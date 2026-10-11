const express = require('express');

const app = express();
const port = 3000;

app.use(express.json());

// Sample train data. The data is kept in memory, so it resets when the server restarts.
const trains = [
  {
    id: 'TR100',
    name: 'Morning Express',
    origin: 'Chennai',
    destination: 'Bengaluru',
    travelDate: '2026-10-20',
    classes: {
      Sleeper: { price: 500, seats: ['S1', 'S2', 'S3', 'S4'] },
      'AC 3 Tier': { price: 1000, seats: ['A1', 'A2', 'A3', 'A4'] }
    }
  },
  {
    id: 'TR200',
    name: 'Evening Express',
    origin: 'Chennai',
    destination: 'Bengaluru',
    travelDate: '2026-10-20',
    classes: {
      Sleeper: { price: 450, seats: ['S1', 'S2', 'S3', 'S4'] },
      'AC 2 Tier': { price: 1400, seats: ['B1', 'B2', 'B3', 'B4'] }
    }
  }
];

const holds = [];
const bookings = [];
let nextHoldNumber = 1;
let nextBookingNumber = 1;

function findTrain(trainId) {
  return trains.find(function (train) {
    return train.id === trainId;
  });
}

function findActiveHold(holdId) {
  const hold = holds.find(function (item) {
    return item.id === holdId;
  });

  if (!hold) {
    return null;
  }

  if (new Date(hold.expiresAt).getTime() <= Date.now()) {
    hold.status = 'expired';
    return null;
  }

  return hold;
}

function getAvailableSeats(train, className) {
  const classDetails = train.classes[className];
  const bookedSeats = [];

  bookings.forEach(function (booking) {
    if (booking.status === 'confirmed' && booking.trainId === train.id && booking.className === className) {
      booking.seatNumbers.forEach(function (seatNumber) {
        bookedSeats.push(seatNumber);
      });
    }
  });

  return classDetails.seats.filter(function (seatNumber) {
    return !bookedSeats.includes(seatNumber);
  });
}

// Search trains by the three required query values.
app.get('/trains/search', function (req, res) {
  const { origin, destination, travelDate } = req.query;

  if (!origin || !destination || !travelDate) {
    return res.status(400).json({ error: 'origin, destination, and travelDate are required' });
  }

  const matchingTrains = trains.filter(function (train) {
    return train.origin.toLowerCase() === origin.toLowerCase()
      && train.destination.toLowerCase() === destination.toLowerCase()
      && train.travelDate === travelDate;
  });

  res.json({ trains: matchingTrains.map(function (train) {
    return {
      id: train.id,
      name: train.name,
      origin: train.origin,
      destination: train.destination,
      travelDate: train.travelDate
    };
  }) });
});

// Show classes, prices, and seats that are not booked yet.
app.get('/trains/:trainId/classes', function (req, res) {
  const train = findTrain(req.params.trainId);

  if (!train) {
    return res.status(404).json({ error: 'Train not found' });
  }

  const classList = Object.keys(train.classes).map(function (className) {
    return {
      name: className,
      price: train.classes[className].price,
      availableSeats: getAvailableSeats(train, className)
    };
  });

  res.json({ trainId: train.id, classes: classList });
});

// Hold selected seats for a short time before payment and booking.
app.post('/holds', function (req, res) {
  const { trainId, className, seatNumbers, userId, holdSeconds } = req.body;
  const train = findTrain(trainId);

  if (!trainId || !className || !Array.isArray(seatNumbers) || seatNumbers.length === 0 || !userId) {
    return res.status(400).json({ error: 'trainId, className, seatNumbers, and userId are required' });
  }

  if (!train) {
    return res.status(404).json({ error: 'Train not found' });
  }

  if (!train.classes[className]) {
    return res.status(400).json({ error: 'Travel class not found' });
  }

  if (new Set(seatNumbers).size !== seatNumbers.length) {
    return res.status(400).json({ error: 'A seat cannot be listed more than once' });
  }

  const availableSeats = getAvailableSeats(train, className);
  const unavailableSeat = seatNumbers.find(function (seatNumber) {
    return !availableSeats.includes(seatNumber);
  });

  if (unavailableSeat) {
    return res.status(409).json({ error: `Seat ${unavailableSeat} is unavailable` });
  }

  const seconds = Number(holdSeconds) > 0 ? Number(holdSeconds) : 60;
  const hold = {
    id: `H${String(nextHoldNumber++).padStart(3, '0')}`,
    trainId,
    className,
    seatNumbers,
    userId,
    status: 'active',
    expiresAt: new Date(Date.now() + seconds * 1000).toISOString()
  };

  holds.push(hold);
  res.status(201).json({ message: 'Seats held temporarily', hold });
});

// Turn an active hold into a booking after a simulated payment.
app.post('/bookings', function (req, res) {
  const { holdId, passengers, paymentStatus, requestId } = req.body;

  if (!holdId || !Array.isArray(passengers) || passengers.length === 0 || !paymentStatus || !requestId) {
    return res.status(400).json({ error: 'holdId, passengers, paymentStatus, and requestId are required' });
  }

  const previousBooking = bookings.find(function (booking) {
    return booking.requestId === requestId;
  });

  if (previousBooking) {
    return res.status(409).json({ error: 'Duplicate booking request', booking: previousBooking });
  }

  const hold = findActiveHold(holdId);

  if (!hold) {
    return res.status(410).json({ error: 'Hold was not found or has expired' });
  }

  if (passengers.length !== hold.seatNumbers.length) {
    return res.status(400).json({ error: 'One passenger is required for each held seat' });
  }

  const invalidPassenger = passengers.find(function (passenger) {
    return !passenger.name || !passenger.age || Number(passenger.age) < 1;
  });

  if (invalidPassenger) {
    return res.status(400).json({ error: 'Each passenger needs a name and a valid age' });
  }

  if (paymentStatus !== 'success' && paymentStatus !== 'failure') {
    return res.status(400).json({ error: "paymentStatus must be 'success' or 'failure'" });
  }

  if (paymentStatus === 'failure') {
    hold.status = 'payment_failed';
    return res.status(402).json({ error: 'Simulated payment failed; booking was not created' });
  }

  const train = findTrain(hold.trainId);
  const availableSeats = getAvailableSeats(train, hold.className);
  const unavailableSeat = hold.seatNumbers.find(function (seatNumber) {
    return !availableSeats.includes(seatNumber);
  });

  if (unavailableSeat) {
    return res.status(409).json({ error: `Seat ${unavailableSeat} is no longer available` });
  }

  const booking = {
    id: `B${String(nextBookingNumber++).padStart(3, '0')}`,
    requestId,
    userId: hold.userId,
    trainId: hold.trainId,
    className: hold.className,
    seatNumbers: hold.seatNumbers,
    passengers,
    paymentStatus: 'success',
    status: 'confirmed',
    createdAt: new Date().toISOString()
  };

  hold.status = 'used';
  bookings.push(booking);
  res.status(201).json({ message: 'Booking created', booking });
});

app.get('/bookings/:bookingId', function (req, res) {
  const booking = bookings.find(function (item) {
    return item.id === req.params.bookingId;
  });

  if (!booking) {
    return res.status(404).json({ error: 'Booking not found' });
  }

  res.json({ booking });
});

app.get('/users/:userId/bookings', function (req, res) {
  const userBookings = bookings.filter(function (booking) {
    return booking.userId === req.params.userId;
  });

  res.json({ userId: req.params.userId, bookings: userBookings });
});

app.delete('/bookings/:bookingId', function (req, res) {
  const booking = bookings.find(function (item) {
    return item.id === req.params.bookingId;
  });

  if (!booking) {
    return res.status(404).json({ error: 'Booking not found' });
  }

  if (booking.status === 'cancelled') {
    return res.status(409).json({ error: 'Booking is already cancelled' });
  }

  booking.status = 'cancelled';
  res.json({ message: 'Booking cancelled', booking });
});

app.get('/', function (req, res) {
  res.json({
    message: 'Railway Booking API is running',
    example: 'Try GET /trains/search?origin=Chennai&destination=Bengaluru&travelDate=2026-10-20'
  });
});

app.listen(port, function () {
  console.log(`Railway booking API is running at http://localhost:${port}`);
});
