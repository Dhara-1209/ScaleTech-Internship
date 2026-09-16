from unittest.mock import patch
from cal import calculate_square_root

@patch("calculator.math.sqrt")
def test_square_root(mock_sqrt):
    mock_sqrt.return_value = 10

    result = calculate_square_root(100)

    assert result == 10
    mock_sqrt.assert_called_once_with(100)