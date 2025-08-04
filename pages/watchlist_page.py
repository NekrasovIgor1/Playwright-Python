import time
from time import sleep

from playwright.sync_api import Page
from pages.base_page import BasePage

class WatchlistPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __CREATE_NEW_LIST_BTN = '[data-testid*="add-to-list-btn"]'
    __LIST_NAME = '[aria-label="List name"]'
    __LIST_NAME_DESCRIPTION = '[data-testid="input-list-description"]'
    __CREATE_BTN = 'section > button > span'
    __YOUR_LIST_BTN = '[data-testid="SidebarList-your"] a h3'
    __LIST_TITLE = '[data-testid="hero__pageTitle"] > span'
    __WATCHLIST_HEADER = '[data-testid="hero__pageTitle"] >span'
    __WATCHLIST_TITLES_NAME = 'h3.ipc-title__text--reduced'
    __MOVIE_TITLE = 'h3.ipc-title__text--reduced'
    __LIST_TYPE = {
        "Titles": 'input[data-testid="input-list-type-TITLES"]',
        "People": 'input[data-testid="input-list-type-PEOPLE"]',
        "Images": 'input[data-testid="input-list-type-IMAGES"]',
        "Videos": 'input[data-testid="input-list-type-VIDEOS"]',
    }
    __PRIVACY = {
        "Public": '[id*="PUBLIC"]',
        "Private": '[id*="PRIVATE"]',
    }

    def create_new_list_btn(self):
        self.click(self.__CREATE_NEW_LIST_BTN)

    def fill_info(self, list_name: str, description: str, list_type: str, privacy: str):
        self.fill_text(self.__LIST_NAME, list_name)
        self.fill_text(self.__LIST_NAME_DESCRIPTION, description)
        time.sleep(2)

        type_locator = self.__LIST_TYPE.get(list_type)
        if type_locator:
            self.check(type_locator)

        privacy_locator = self.__PRIVACY.get(privacy)
        if privacy_locator:
            self.check(privacy_locator)
        self.click(self.__CREATE_BTN)


    def get_list_title(self):
        return self.inner_text(self.__LIST_TITLE)

    def create_new_list(self,list_name: str, description: str, list_type: str, privacy: str):
        self.click(self.__CREATE_NEW_LIST_BTN)
        self.fill_text(self.__LIST_NAME, list_name)
        self.fill_text(self.__LIST_NAME_DESCRIPTION, description)
        type_locator = self.__LIST_TYPE.get(list_type)
        if type_locator:
            self.check(type_locator)
        privacy_locator = self.__PRIVACY.get(privacy)
        if privacy_locator:
            self.check(privacy_locator)
        self.click(self.__CREATE_BTN)
        time.sleep(2)

    def your_list_btn(self):
        time.sleep(4)
        self.click(self.__YOUR_LIST_BTN)

    def get_watchlist_titles(self) -> list[str]:
        movie_elements = self.get_locator(self.__WATCHLIST_TITLES_NAME)
        return [title.split('.')[-1].strip() for title in movie_elements.all_inner_texts()]

    def movie_titles(self):
        titles = self.get_locator(self.__MOVIE_TITLE).all_inner_texts()
        return [title.split('.')[-1].strip() for title in titles]

    def page_header(self):
        return self.get_text(self.__WATCHLIST_HEADER)














