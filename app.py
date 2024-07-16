from flask import Flask, jsonify, request
from scraper import scrape_jobs
from request_handler import fetch_job_data
from logging_config import setup_logging

import logging

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/jobs', methods=['GET'])
def get_jobs_query():
    """
    Endpoint to get job listings based on search query and location.

    This endpoint receives GET requests with optional query parameters 'q' (search query)
    and 'location'. It constructs a URL to fetch job data, scrapes the job listings
    from the fetched HTML content, and returns the job listings as a JSON response.

    Query Parameters:
        q (str): The search query. Default is 'software'.
        location (str): The location filter. Default is an empty string.

    Returns:
        JSON: A JSON response containing the list of job listings or an error message.
    """
    logger.info("Endpoint hit (get_jobs_query)")
    search_query = request.args.get('q', default='software', type=str)
    location = request.args.get('location', default='', type=str)
    url = f"https://us241.dayforcehcm.com/CandidatePortal/EN-us/pgh2o?q={search_query}&location={location}"

    try:
        html_content = fetch_job_data(url)
        jobs = scrape_jobs(html_content)
        logger.info("Endpoint Success (get_jobs_query)")
        return jsonify(jobs)
    except Exception as e:
        logger.error(f"Endpoint Failure (get_jobs_query) {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8081)
