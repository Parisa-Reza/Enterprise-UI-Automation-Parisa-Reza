import pytest
import random
from pages.home_page import HomePage
from pages.detail_page import DetailPage

@pytest.mark.regression
def test_book_data_consistency_validation(page):
    """
    TCaptures titles and prices for 5 random books from the homepage catalog, opens their detail pages, and verifies that the captured text criteria match exactly.
    """
    home = HomePage(page)
    detail = DetailPage(page)
    
    home.navigate_to_home()
  
    books_catalog = home.get_book_titles_and_prices()
    assert len(books_catalog) >= 5, "Insufficient book items discovered for data consistency audit."
    sampled_entries = random.sample(books_catalog, 5)

    for entry in sampled_entries:
        homepage_title = entry["title"]
        homepage_price = entry["price"]
        
        # Open the book details page view
        home.click_book_by_index(entry["index"])
        page.wait_for_load_state("domcontentloaded")
        
       
        detail_title = detail.get_product_title()
        detail_price = detail.get_product_price()
        assert homepage_title == detail_title, f"Data mismatch. Homepage Title: '{homepage_title}' but Detail Title: '{detail_title}'"
        assert homepage_price == detail_price, f"Data mismatch. Homepage Price: '{homepage_price}' but Detail Price: '{detail_price}'"
        
        home.navigate_to_home()