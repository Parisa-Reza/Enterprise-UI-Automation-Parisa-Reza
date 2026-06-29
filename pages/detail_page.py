from pages.base_page import BasePage

class DetailPage(BasePage):
    """
    Extracts text parameters from specific book layout item .
    """
    def __init__(self, page):
        super().__init__(page)
        # Target matching components based on explicit source class strings
        self.main_title = page.locator("div.product_main h1")
        self.main_price = page.locator("div.product_main p.price_color")
        self.stock_status = page.locator("div.product_main p.instock.availability")

    def get_product_title(self):
        return self.main_title.inner_text().strip()

    def get_product_price(self):
        return self.main_price.inner_text().strip()

    def is_product_info_visible(self):
        return self.main_title.is_visible() and self.stock_status.is_visible()