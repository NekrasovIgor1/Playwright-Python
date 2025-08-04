import time

from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.top_nav_bar import TopNavBar

class MainPage(TopNavBar,BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __MENU = 'div.drawer__panel[aria-hidden="false"]'
    __TOP10_HEADER = ".top-ten h3"
    __MOVIE_CARD_TOP10 = '.top-ten .ipc-poster-card'
    __ADD_TO_WATCHLIST_BNT = '[data-testid="poster-watchlist-ribbon-add"]'
    __MOVIE_TITLE_IN_CARD = '[data-testid="title"]'
    __TOP_PICKS_TITLE = '.top-picks h3'
    __MOVIE_CARD_TOP_PICKS = '.top-picks .ipc-poster-card'
    __EXPLORE_SECTION = '[data-testid="streaming-picks-shoveler"]'
    __EXPLORE_TITLE = '[data-testid="exploreStreaming_title"] h3'
    __EXPLORE_CARD ='[data-testid="streaming-picks-shoveler"] .ipc-poster-card'
    __EXPLORE_CARD_TITLE = '.streaming-picks [data-testid="title"]'


    def menu(self):
        return self.is_visible(self.__MENU)

    def scroll_to_element(self,pixels:int,locator):
        self.scroll_by_pixels(pixels)
        element = self.get_locator(locator)
        element.scroll_into_view_if_needed()

    # add movie by index from top10 this week section
    def add_movie_to_watchlist_by_index_from_top10(self, index: int):
        self.scroll_to_element(1500,self.__TOP10_HEADER)
        self.wait_for_locator(self.__MOVIE_CARD_TOP10)
        movie_cards = self.get_locator(self.__MOVIE_CARD_TOP10)
        count = movie_cards.count()
        if index < 1 or index > count:
            raise ValueError(f"Invalid movie index: {index}. Must be between 1 and {count}")
        card = movie_cards.nth(index - 1)
        movie_title = card.locator(self.__MOVIE_TITLE_IN_CARD).inner_text().strip()
        movie_title = movie_title.split('.', 1)[-1].strip()
        self.click_inside(card, self.__ADD_TO_WATCHLIST_BNT)
        return movie_title

    # add movie by index from top picks section
    def add_movie_to_watchlist_by_index_from_top_picks(self, index: int):
        self.scroll_to_element(1400,self.__TOP_PICKS_TITLE)
        self.wait_for_locator(self.__MOVIE_CARD_TOP_PICKS)
        movie_cards = self.get_locator(self.__MOVIE_CARD_TOP_PICKS)
        count = movie_cards.count()
        if index < 1 or index > count:
            raise ValueError(f"Invalid movie index: {index}. Must be between 1 and {count}")
        card = movie_cards.nth(index - 1)
        movie_title = card.locator(self.__MOVIE_TITLE_IN_CARD).inner_text().strip()
        movie_title = movie_title.split('.', 1)[-1].strip()
        self.click_inside(card, self.__ADD_TO_WATCHLIST_BNT)
        return movie_title

        # add movie by index from explore section

    def add_movie_to_watchlist_by_index_from_explore_section(self, index: int):
        self.scroll_to_element(2500, self.__EXPLORE_TITLE)
        self.wait_for_locator(self.__EXPLORE_CARD)
        movie_cards = self.get_locator(self.__EXPLORE_CARD)
        count = movie_cards.count()
        if index < 1 or index > count:
            raise ValueError(f"Invalid movie index: {index}. Must be between 1 and {count}")
        card = movie_cards.nth(index - 1)
        movie_title = card.locator(self.__MOVIE_TITLE_IN_CARD).inner_text(timeout=10000).strip()
        movie_title = movie_title.split('.', 1)[-1].strip()
        self.click_inside(card, self.__ADD_TO_WATCHLIST_BNT)
        return movie_title

    def click_on_video_from_top_picks_section(self, index: int):
        self.scroll_to_element(1400, self.__TOP_PICKS_TITLE)
        self.wait_for_locator(self.__MOVIE_CARD_TOP_PICKS)
        movie_cards = self.get_locator(self.__MOVIE_CARD_TOP_PICKS)
        count = movie_cards.count()
        if index < 1 or index > count:
            raise ValueError(f"Invalid movie index: {index}. Must be between 1 and {count}")
        card = movie_cards.nth(index - 1)
        time.sleep(2)









