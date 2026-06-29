import pytest
from pages.home_page import HomePage

@pytest.mark.regression
def test_product_image_and_pagination_validation(page):
    """
    Verify that product images are rendered correctly and contain the required attributes.
    """
    home = HomePage(page)
    home.navigate_to_home()

    max_pages = 5
    current_page = 1


    while current_page <= max_pages:
        img_count = home.product_images.count()
        assert img_count > 0, f"No product image on catalog page: {current_page}"

        for i in range(img_count):
            img = home.product_images.nth(i)
            assert img.is_visible() is True, f"Image at index {i} on page {current_page} is not visible."
            
  
            src = img.get_attribute("src")
            alt = img.get_attribute("alt")
            css_class = img.get_attribute("class")

            assert src and len(src.strip()) > 0, f"Missing src parameter at index {i}."
            assert alt and len(alt.strip()) > 0, f"Missing alt  parameter at index {i}."
            assert "thumbnail" in (css_class or ""), f"Expected 'thumbnail' class missing at index {i}."

        #if the last page index is reached 
        if not home.handle_pagination_next():
            break
        current_page += 1