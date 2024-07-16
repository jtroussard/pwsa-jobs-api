import pytest
import requests
import requests_mock
from request_handler import fetch_job_data
from unittest.mock import Mock


@pytest.fixture
def url():
    return "http://example.com/jobs"

def test_fetch_job_data_success(url):
    with requests_mock.Mocker() as m:
        html_content = "<html><body>Job Listings</body></html>"
        m.get(url, text=html_content)
        result = fetch_job_data(url)
        assert result == html_content

def test_fetch_job_data_raises_http_error(mocker):
    url = "http://example.com"
    
    # Mock the requests.get call to return a response with a 404 status code
    mock_response = Mock(spec=requests.Response)
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Client Error: Not Found for url")
    
    mocker.patch("requests.get", return_value=mock_response)

    # Assert that fetch_job_data raises a requests.HTTPError
    with pytest.raises(requests.HTTPError):
        fetch_job_data(url)
