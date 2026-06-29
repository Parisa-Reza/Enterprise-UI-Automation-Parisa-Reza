import pytest
import random
from pages.home_page import HomePage
from pages.detail_page import DetailPage

@pytest.mark.regression
def test_random_book_navigation_and_consistency(page):
    """
   Navigate to homepage, collect all available book items, randomly select 5 books.y and matches metadata values dynamically to assert data consistency.
    """
    home = HomePage(page)
    detail = DetailPage(page)
    
    home.navigate_to_home()
    books_catalog = home.get_book_titles_and_prices()
    
    assert len(books_catalog) >= 5, "Insufficient products layout elements found."
    sampled_entries = random.sample(books_catalog, 5)

    for entry in sampled_entries:

        home.click_book_by_index(entry["index"])
        page.wait_for_load_state("domcontentloaded")
        

        assert detail.is_product_info_visible() is True
        
        assert entry["title"] == detail.get_product_title(), f"Mismatch at title header context tracking!"
    
        home.navigate_to_home()