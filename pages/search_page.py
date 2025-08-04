from playwright.sync_api import Page
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    # selector for the search result header
    __HEADER_TEXT = '.ipc-page-section h1'
    # selector for category section header like 'Titles'
    __CATEGORY_TEXT = ' .ipc-page-grid__item--span-2 h3'
    # First result title
    __FIRST_RESULT = '.ipc-metadata-list--base >li:nth-child(1)'

    def get_header_text(self) -> str:
        return self.get_text(self.__HEADER_TEXT)

    def get_category_text(self) -> str:
        return self.get_locator(self.__CATEGORY_TEXT).nth(0).inner_text()

    def get_first_result_text(self) -> str:
        return self.get_locator(self.__FIRST_RESULT).nth(0).inner_text()
