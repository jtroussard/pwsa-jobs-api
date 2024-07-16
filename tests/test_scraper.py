import pytest
from scraper import scrape_jobs

@pytest.fixture
def html_content():
    return '''
    <ul class="search-results">
        <li class="search-result">
            <div class="posting-title">
                <h2><a href="#">Job Title 1</a></h2>
            </div>
            <div class="posting-subtitle">
                <div>Location 1</div>
            </div>
            <div class="posting-date">Posted Date 1</div>
            <div class="posting-description">
                <span>Description 1</span>
            </div>
        </li>
        <li class="search-result">
            <div class="posting-title">
                <h2><a href="#">Job Title 2</a></h2>
            </div>
            <div class="posting-subtitle">
                <div>Location 2</div>
            </div>
            <div class="posting-date">Posted Date 2</div>
            <div class="posting-description">
                <span>Description 2</span>
            </div>
        </li>
    </ul>
    '''

def test_scrape_jobs(html_content):
    jobs = scrape_jobs(html_content)
    assert isinstance(jobs, list)
    assert len(jobs) == 2

    assert jobs[0]['title'] == 'Job Title 1'
    assert jobs[0]['location'] == 'Location 1'
    assert jobs[0]['date_posted'] == 'Posted Date 1'
    assert jobs[0]['description'] == 'Description 1'

    assert jobs[1]['title'] == 'Job Title 2'
    assert jobs[1]['location'] == 'Location 2'
    assert jobs[1]['date_posted'] == 'Posted Date 2'
    assert jobs[1]['description'] == 'Description 2'
