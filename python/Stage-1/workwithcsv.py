import csv
with open("text.csv","a",newline="") as files:
    writer=csv.writer(files)

    writer.writerow(["vaishvi","19","88"])

with open("text.csv","r") as f:
    reader=csv.reader(f)

    for i in reader:
        print(i)

with open("text.csv","r") as fi:
    reder=csv.DictReader(fi)

    for row in reder:
        print(row)


