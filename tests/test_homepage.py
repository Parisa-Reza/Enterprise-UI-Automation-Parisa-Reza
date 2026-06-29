import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage

@pytest.mark.smoke
def test_homepage_validation(page):
    """
    Ensures that browser routing coordinates correctly matching base expected constants.
    """
    home = HomePage(page)
    home.navigate_to_home() # from basepage

    assert home.get_current_url() == "https://books.toscrape.com/index.html"
    assert "All products" in home.get_page_title()

    expect(home.books_section).to_be_visible()
    assert home.get_book_count() > 0 # from homepage

    headings = home.get_all_heading_texts()
    assert len(headings) > 0
    for text in headings:
        assert len(text) > 0