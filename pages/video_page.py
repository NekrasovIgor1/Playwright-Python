from playwright.sync_api import Page
from pages.base_page import BasePage

class VideoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    # rate locators and buttons:
    __RATE_BTN = '.iWItnY [aria-label*="Rate"], .iWItnY [aria-label*="rating"]'
    __RATING_STARS = {
        '1': 'button[aria-label="Rate 1"]',
        '2': 'button[aria-label="Rate 2"]',
        '3': 'button[aria-label="Rate 3"]',
        '4': 'button[aria-label="Rate 4"]',
        '5': 'button[aria-label="Rate 5"]',
        '6': 'button[aria-label="Rate 6"]',
        '7': 'button[aria-label="Rate 7"]',
        '8': 'button[aria-label="Rate 8"]',
        '9': 'button[aria-label="Rate 9"]',
        '10': 'button[aria-label="Rate 10"]',
    }
    __RATE_CONFIRM_BTN = '.ipc-rating-prompt__rate-button'
    __STARS_AMOUNT_RATED = ''
    __YOUR_RATINGS = 'button span div span'
    # add to watchlist locators and buttons:
    __ADD_TO_WATCHLIST_BTN = '[data-testid="tm-box-wl-button"]'
    __WATCHLIST_BTN_V_SIGN = '[data-testid*="button"] [d^="M9"]'
    __WATCHLIST_BTN_TEXT = '[data-testid="tm-box-wl-text"]'  # "In watchlist" \ "Add to Watchlist" text
    __POSTER_V_SIGN_WATCHLIST = '[data-testid*="poster-watchlist" ] [d^="M9"]'
    __MARK_AS_WATCHED_BTN = '[data-testid*="watched-button"]'
    __WATCHED_BTN_TEXT = '[data-testid*="watched-button"] span'
    __REMOVE_RATINGS = '.ipc-rating-prompt__container button.ipc-btn--core-baseAlt'

    def rate_btn_click(self):
        self.click(self.__RATE_BTN)

    def rate_stars(self,stars_amount:str):
        # hide the overlay div that blocks click
        self.evaluate_script("document.querySelector('.ipc-starbar__touch').style.display = 'none'")
        star_locator = self.__RATING_STARS.get(stars_amount)
        self.click(star_locator)
        self.click(self.__RATE_CONFIRM_BTN)

    def get_your_ratings(self):
        return self.get_locator(self.__YOUR_RATINGS).first.inner_text()

    def add_to_watchlist_btn(self):
        self.click(self.__ADD_TO_WATCHLIST_BTN)

    def is_watchlist_checked(self) -> bool:
        locator = 'button[data-testid="tm-box-wl-button"] svg path[d^="M9 16.2"]'
        return self.get_locator(locator).is_visible()

    def is_watchlist_text_in(self) -> bool:
        return self.get_locator(self.__WATCHLIST_BTN_TEXT).inner_text().strip() == "In Watchlist"

    def is_poster_v_visible(self) -> bool:
        return self.get_locator(self.__POSTER_V_SIGN_WATCHLIST).is_visible()

    def mark_as_watched(self):
        self.get_locator(self.__MARK_AS_WATCHED_BTN).first.click()

    def watched_btn_text(self):
        return self.get_text(self.__WATCHED_BTN_TEXT)

    def remove_ratings(self):
        self.click(self.__REMOVE_RATINGS)
