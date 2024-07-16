import requests
import logging

logger = logging.getLogger(__name__)

def fetch_job_data(url):
    """
    Fetches job data from the provided URL.

    Makes a GET request to the specified URL and returns the response content
    if the request is successful. Logs the request and handles any exceptions
    that may occur during the request process.

    Args:
        url (str): The URL to fetch job data from.

    Returns:
        str: The HTML content of the job listings page if the request is successful.

    Raises:
        requests.RequestException: An error occurred during the HTTP request.
    """
    logger.info("bear town")
    try:
        logger.info(f"Request made (fetch_job_data): {url}")
        response = requests.get(url)
        response.raise_for_status() 
        logger.info(f"Request completed successfully (fetch_job_data): {url}")
        return response.text
    except Exception as e:
        logger.error(f"Request failed (fetch_job_data): {e}", exc_info=True)
        raise
