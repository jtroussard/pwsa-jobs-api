import requests
import logging

logger = logging.getLogger(__name__)

def fetch_job_data(url):
    try:
        logger.info(f"Request made (fetch_job_data): {url}")
        response = requests.get(url)
        response.raise_for_status() 
        logger.info(f"Request completed successfully (fetch_job_data): {url}")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Request failed (fetch_job_data): {e}", exc_info=True)
