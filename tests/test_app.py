import pytest
import requests
from unittest.mock import patch, Mock
from app import app  # Adjust this import according to your module's name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_jobs_query_success(client):
    url = "https://us241.dayforcehcm.com/CandidatePortal/EN-us/pgh2o?q=software&location="
    
    # Mock the fetch_job_data function to return a predefined HTML content
    mock_html_content = "<html><body>Mock job listings</body></html>"
    with patch('app.fetch_job_data', return_value=mock_html_content):
        # Mock the scrape_jobs function to return a predefined list of jobs
        mock_jobs = [{'title': 'Software Engineer', 'location': 'Pittsburgh', 'description': 'Develop software solutions.'}]
        with patch('app.scrape_jobs', return_value=mock_jobs):
            response = client.get('/api/jobs')
            assert response.status_code == 200
            assert response.json == mock_jobs

def test_get_jobs_query_failure_fetch_data(client):
    url = "https://us241.dayforcehcm.com/CandidatePortal/EN-us/pgh2o?q=software&location="
    
    # Mock the fetch_job_data function to raise an HTTPError
    with patch('app.fetch_job_data', side_effect=requests.HTTPError("404 Client Error: Not Found for url")):
        response = client.get('/api/jobs')
        assert response.status_code == 500
        assert 'error' in response.json

def test_get_jobs_query_failure_scrape_jobs(client):
    url = "https://us241.dayforcehcm.com/CandidatePortal/EN-us/pgh2o?q=software&location="
    
    # Mock the fetch_job_data function to return a predefined HTML content
    mock_html_content = "<html><body>Mock job listings</body></html>"
    with patch('app.fetch_job_data', return_value=mock_html_content):
        # Mock the scrape_jobs function to raise an exception
        with patch('app.scrape_jobs', side_effect=Exception("Scraping error")):
            response = client.get('/api/jobs')
            assert response.status_code == 500
            assert 'error' in response.json
