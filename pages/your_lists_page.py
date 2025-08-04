import time

from playwright.sync_api import Page
from pages.base_page import BasePage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class YourListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __KEBAB_AREA = '[data-testid$="list-content"]'
    __KEBAB_MENU = 'button'
    __LIST_NAME = 'a.ipc-metadata-list-summary-item__t'
    __LIST_AREA = 'li.ipc-metadata-list-summary-item'
    __KEBAB_VIEW_OPTION = '#list-dropdown-option-view'
    __KEBAB_DELETE_BTN = '#list-dropdown-option-delete'
    __DELETE_CONFIRM_BTN   = '[data-testid*="delete-button"]'
    __LiNK_BAR = '#text-input__1'
    __SEARCH_BAR = 'input[class="ipc-textinput__input"]'
    __ADD_BTN = '[data-testid$="input-button"]'
    __PLUS_BTN = '#react-autowhatever-1--item-0'
    __CREATE_NEW_LIST_BTN = '[data-testid*="add-to-list-btn"]'
    __MOVIE_TITLE = "h3.ipc-title__text.ipc-title__text--reduced"
    __IMAGE_TITLE = 'div[class*="sc-a28800e7"] h3'
    __PEOPLE_TITLE = 'div[class*="sc-a28800e7"] h3'
    __YOUR_LIST_PAGE_HEADER = '[data-testid="hero__primary-text"]'
    #for adit options
    __MOVIES_AREA = 'li.ipc-metadata-list-summary-item'
    __MOVIE_NAME = '[data-testid="eli-title"]'
    __CHECK_BOX = 'input[data-testid="eli-check-box"]'
    __MOVE_BTN = 'button[data-testid="list-edit-move-items"]'
    __COPY_BTN = '[data-testid="list-edit-copy-items"]'
    __DELETE_BTN = '[data-testid="list-edit-delete-items"]'
    __DELETE_CONFIRM = '[data-testid="dlp-delete-btn"]'
    __NEW_LIST_SELECTOR_TEMPLATE = '[aria-label="{list_name}"]'
    __SAVE_BTN = '[data-testid="dlp-save-btn"]'

    def delete_list(self, list_name: str):
        time.sleep(3)
        self.reload_page()
        list_cards = self.get_locator(self.__LIST_AREA)
        for i in range(list_cards.count()):
            title_label = list_cards.nth(i).locator(self.__LIST_NAME)
            if title_label.inner_text().strip() == list_name:
                self.click_inside(list_cards.nth(i), self.__KEBAB_MENU)
                self.click(self.__KEBAB_DELETE_BTN)
                self.click(self.__DELETE_CONFIRM_BTN)
                break
        else:
            raise Exception(f"List with name '{list_name}' was not found.")

    # Kebab menu btn
    def kebab_menu_ntn(self):
        self.click(self.__KEBAB_MENU)

    def kebab_menu_view_option(self):
        self.click(self.__KEBAB_VIEW_OPTION)

    # Check if a list with the given name still exists in the user's list page.
    def is_list_exist(self, list_name_to_delete: str) -> bool:
        try:
            self.get_locator(f"text={list_name_to_delete}").wait_for(timeout=3000)
            return True
        except PlaywrightTimeoutError:
            return False

    # use for image and videos lists
    def add_link_to_list(self,link:str):
        self.fill_text(self.__LiNK_BAR,link)
        self.click(self.__ADD_BTN)

    # use for titles and people lists
    def add_from_search_to_list(self,name:str):
        self.fill_text(self.__SEARCH_BAR,name)
        self.click(self.__PLUS_BTN)


    def select_movie_for_move(self,movie_name,new_list_name):
        movie_area_list = self.get_locator(self.__MOVIES_AREA)
        for i in range(movie_area_list.count()):
            movie_label = movie_area_list.nth(i).locator(self.__MOVIE_NAME)
            if movie_name in movie_label.inner_text():
                self.check_inside(movie_area_list.nth(i), self.__CHECK_BOX)
                break
        self.click(self.__MOVE_BTN)
        list_selector = self.__NEW_LIST_SELECTOR_TEMPLATE.format(list_name=new_list_name)
        self.click(list_selector)
        self.click(self.__SAVE_BTN)
        time.sleep(5)

    def select_movie_for_copy(self,movie_name,new_list_name):
        movie_area_list = self.get_locator(self.__MOVIES_AREA)
        for i in range(movie_area_list.count()):
            movie_label = movie_area_list.nth(i).locator(self.__MOVIE_NAME)
            if movie_name in movie_label.inner_text():
                self.check_inside(movie_area_list.nth(i), self.__CHECK_BOX)
                break
        self.click(self.__COPY_BTN)
        list_selector = self.__NEW_LIST_SELECTOR_TEMPLATE.format(list_name=new_list_name)
        self.click(list_selector)
        self.click(self.__SAVE_BTN)
        time.sleep(5)

    def select_movie_for_delete(self,movie_name,new_list_name):
        movie_area_list = self.get_locator(self.__MOVIES_AREA)
        for i in range(movie_area_list.count()):
            movie_label = movie_area_list.nth(i).locator(self.__MOVIE_NAME)
            if movie_name.lower() in movie_label.inner_text().lower():
                self.check_inside(movie_area_list.nth(i), self.__CHECK_BOX)
                break
        self.click(self.__DELETE_BTN)
        self.click(self.__DELETE_CONFIRM)
        time.sleep(5)

    def view_list(self, list_name):
        kebab_area_list = self.get_locator(self.__LIST_AREA)

        for i in range(kebab_area_list.count()):
            current_name_element = kebab_area_list.nth(i).locator(self.__LIST_NAME)
            actual_name = current_name_element.inner_text()

            if list_name in actual_name:
                self.click_inside(kebab_area_list.nth(i), self.__KEBAB_MENU)
                self.click(self.__KEBAB_VIEW_OPTION)
                break
        else:
            raise Exception(f"List with name '{list_name}' was not found.")

    def movie_titles(self):
        titles = self.get_locator(self.__MOVIE_TITLE).all_inner_texts()
        return [title.split('.')[-1].strip() for title in titles]

    def image_title(self):
        return self.get_locator(self.__IMAGE_TITLE).inner_text()

    def people_title(self):
        return self.get_locator(self.__PEOPLE_TITLE).inner_text()

    def page_header(self):

        return self.get_text(self.__YOUR_LIST_PAGE_HEADER)









