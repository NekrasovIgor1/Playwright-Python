from playwright.sync_api import Page
from pages.base_page import BasePage

class TopNavBar(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    # bar buttons:
    __SIGN_IN_BTN = 'div[class*="userMenu"] > a'
    __PROFILE_NAME = 'span.imdb-header__account-toggle--logged-in.navbar__user-name'
    __WATCHLIST_BTN = 'div[class*="watchlist-button"]'
    __BANNER_BTN = 'a.imdb-header__logo-link--large#home_img_holder[aria-label="Home"]'
    __MENU_BTN = '#imdbHeader-navDrawerOpen > span'
    __IMDBPRO_BTN = '[class*="elTkBv navbar__imdbpro"]'
    #profile:
    __PROFILE_BTN = '[class*="o navbar__flyout--breakpoint-m"]'
    __USER_MENU_LINKS = {
        'your_profile': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(1)',
        'your_watchlist': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(2)',
        'your_ratings': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(3)',
        'your_lists': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(4)',
        'your_watch_history': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(5)',
        'account_settings': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(6)',
        'sign_out': 'ul[class*="imdb-header__account-menu"] a.ipc-list__item:nth-of-type(7)',
    }
    # search locators:
    __SEARCH_CATEGORY = {
        "All": '.searchCatSelector > li:nth-child(1)',
        "Titles": '.searchCatSelector > li:nth-child(2)',
        "TV episodes": '.searchCatSelector > li:nth-child(3)',
        "Celebs": '.searchCatSelector > li:nth-child(4)',
        "Companies": '.searchCatSelector > li:nth-child(5)',
        "Keywords": '.searchCatSelector > li:nth-child(6)',
    }
    __ADVANCED_SEARCH_CATEGORY = '.searchCatSelector a'
    __CATEGORY_SELECTOR_BTN  = '#nav-search-form [data-testid="category-selector-button"]'
    __SEARCH_PROMPT = '#suggestion-search'
    __SEARCH_BTN = '#suggestion-search-button'
    __SEARCH_AUTO_SUGGESTION_1  = '#react-autowhatever-navSuggestionSearch--item-0' #firs result from menu

    def sign_in_btn(self):
        self.click(self.__SIGN_IN_BTN)

    # name next to profile btn (sign in btn)
    def get_tex_profile_name(self):
        return self.get_text(self.__PROFILE_NAME)

    def watchlist_btn(self):
        self.click(self.__WATCHLIST_BTN)

    def banner_btn(self):
        self.click(self.__BANNER_BTN)

    def menu_btn(self):
        self.click(self.__MENU_BTN)

    def imdbpro_btn(self):
        self.click(self.__IMDBPRO_BTN)

        # search by category and name, click on search btn
    def search_by_category_and_name(self, category: str, text: str):
        self.click(self.__CATEGORY_SELECTOR_BTN)
        category_locator = self.__SEARCH_CATEGORY.get(category)
        if category_locator:
            self.click(category_locator)
        else:
            raise ValueError(f"Category '{category}' is not supported")
        self.fill_text(self.__SEARCH_PROMPT, text)
        self.click(self.__SEARCH_BTN)

        # search by category and name, click on first search result from autosuggestion menu
    def search_category_and_name_click(self, category: str, text: str):
        self.click(self.__CATEGORY_SELECTOR_BTN)
        category_locator = self.__SEARCH_CATEGORY.get(category)
        if category_locator:
            self.click(category_locator)
        else:
            raise ValueError(f"Category '{category}' is not supported")
        self.fill_text(self.__SEARCH_PROMPT, text)
        self.click(self.__SEARCH_AUTO_SUGGESTION_1)

    def profile_btn(self):
        self.click(self.__PROFILE_BTN)

    def click_user_menu_item(self, item_name: str):
        selector = self.__USER_MENU_LINKS.get(item_name)
        if not selector:
            raise ValueError(f"Invalid menu item: '{item_name}'")
        self.click(selector)

    def advanced_search_btn(self):
        self.click(self.__CATEGORY_SELECTOR_BTN)
        #self.get_locator(self.__ADVANCED_SEARCH_CATEGORY).hover()
        self.click(self.__ADVANCED_SEARCH_CATEGORY)


