import pytest
from unittest.mock import patch

from sxi_l4.main import app

# @pytest.fixture
# def mock_fit_wharton2025(mocker):
#     return mocker.patch('sxi_l4.fit.Fit.wharton2025')

def test_fit_rasies_error_invalid_input():
    with pytest.raises(FileNotFoundError):
        app("fit non_existent_file.ext")

@patch("sxi_l4.fit.Fit.wharton2025")
def test_fit_calls_fit_wharton2025(mock_fit_wharton2025):
    mock_fit_wharton2025.return_value = 15
    with pytest.raises(SystemExit):
        app("fit data/input.fits")
    mock_fit_wharton2025.assert_called()