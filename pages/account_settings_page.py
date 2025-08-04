from playwright.sync_api import Page
from pages.base_page import BasePage


class YourAccountSettingsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    __HEADER_TEXT = '[data-testid="pageHero-titleBlock-container" ] h1'

    def page_header(self):
        return self.get_text(self.__HEADER_TEXT)