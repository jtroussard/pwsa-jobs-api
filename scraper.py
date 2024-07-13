from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def scrape_jobs(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    jobs = []
    logger.info("Initialized")

    logger.info("Starting to scrape")
    for job_element in soup.select('ul.search-results li.search-result'):
        logger.info("... scraping")
        title = job_element.select_one('.posting-title h2 a').get_text(strip=True)
        location = job_element.select_one('.posting-subtitle div').get_text(strip=True)
        date_posted = job_element.select_one('.posting-date').get_text(strip=True)
        description = job_element.select_one('.posting-description span').get_text(strip=True)
        
        job = {
            'title': title,
            'location': location,
            'date_posted': date_posted,
            'description': description
        }
        jobs.append(job)

    logger.info(f"Scraping complete. Number of jobs found: {len(jobs)}")
    return jobs
