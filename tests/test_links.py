import pytest
from pages.home_page import HomePage

@pytest.mark.regression
def test_hyperlink_broken_link_validation(page):
    """
    Extracts resolved reference URLs from the utility and checkas a sample selection set to ensure there are no broken links (404s.
    """
    home = HomePage(page)
    home.navigate_to_home()
    
    all_links = home.collect_all_href_links()
    assert len(all_links) > 0, "No hyperlink  were extracted from the page."
    
    for link in all_links[:10]:
        # Use Playwright's native API request context forsending a direct GET request to the URL. This executes in milliseconds .it skips rendering images, executing JS, or parsing CSS 
        response = page.request.get(link)
        assert response.ok, f"Broken link found at: {link} (Code Status: {response.status})"