import requests

class BasePage:
    """
   purpose is to group together common, reusable browser actions so that individual page classes don't have to duplicate this core logic.
    """
    def __init__(self, page):
        self.page = page
        self.base_url = "https://books.toscrape.com/index.html"

    def navigate_to_home(self):
        self.page.goto(self.base_url, wait_until="domcontentloaded")

    def get_current_url(self):
        return self.page.url

    def get_page_title(self):
        return self.page.title().strip()