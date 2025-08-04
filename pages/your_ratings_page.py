from playwright.sync_api import Page
from pages.base_page import BasePage

class YourRatingsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __HEADER_TEXT = '[data-testid="hero__primary-text"]'

    def page_header(self):
        return self.get_text(self.__HEADER_TEXT)