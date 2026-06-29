from pages.base_page import BasePage
from utils.link_validator import resolve_absolute_url

class HomePage(BasePage):
    """
    Drives selectors and actions on the product browse catalog layout grid.
    """
    def __init__(self, page):
        super().__init__(page)
        self.all_headings = page.locator("h1, h2, h3, h4, h5, h6")
        self.books_section = page.locator("ol.row")
        self.book_items = page.locator("article.product_pod")
        self.all_links = page.locator("a")
        self.product_images = page.locator("article.product_pod .image_container img")
        self.next_button = page.locator("li.next a")

    def get_all_heading_texts(self):
        return [text.strip() for text in self.all_headings.all_inner_texts() if text.strip()]

    def get_book_count(self):
        return self.book_items.count()

    def get_book_titles_and_prices(self):
        """ loops through the entire page grid to get info """
        books_data = []
        count = self.get_book_count()
        for i in range(count):
            pod = self.book_items.nth(i)
            title = pod.locator("h3 a").get_attribute("title")
            price = pod.locator("p.price_color").inner_text()
            books_data.append({
                "index": i, 
                "title": title.strip() if title else "", 
                "price": price.strip()
            })
        return books_data

    def click_book_by_index(self, index):
        self.book_items.nth(index).locator("h3 a").click()


    def collect_all_href_links(self):
        """
        Extracts all reference links found across the page document,
        delegating the URL mapping logic to the utils validation layer.
        """
        hrefs = []
        count = self.all_links.count()
        
        for i in range(count):
            raw_href = self.all_links.nth(i).get_attribute("href")
            
            resolved_url = resolve_absolute_url(raw_href)
            if resolved_url:
                hrefs.append(resolved_url)
                        
        return list(set(hrefs))
    def handle_pagination_next(self):
        """Automatically manages moving to the next page. It checks if a "Next" button exists. If it does, it clicks it, waits until the next page’s HTML structures load fully """
        if self.next_button.is_visible():
            self.next_button.click()
            self.page.wait_for_load_state("domcontentloaded")
            return True
        return False