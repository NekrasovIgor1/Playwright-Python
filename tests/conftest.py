import pytest

from pages.watchlist_page import WatchlistPage
from pages.your_lists_page import YourListPage
from utils.config_reader import ConfigReader
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.top_nav_bar import TopNavBar
from pages.imbd_pro_page import ImdbProPage
from pages.search_page import SearchPage
from pages.video_page import VideoPage
from pages.profile_page import ProfilePage
from pages.your_ratings_page import YourRatingsPage
from pages.your_watch_history_page import YourWatchHistoryPage
from pages.account_settings_page import YourAccountSettingsPage
from pages.advanced_search_page import AdvancedSearchPage


@pytest.fixture(scope="class")
def setup_page_class(request, browser):
    page = browser.new_page() 
    page.set_default_timeout(60000)  
    page.set_default_navigation_timeout(60000)
    url = ConfigReader.read_config("global", "url")
    page.goto(url, timeout=60000, wait_until="domcontentloaded")
    request.cls.page = page
    request.cls.main_page = MainPage(page)
    request.cls.top_nav_bar = TopNavBar(page)
    request.cls.sign_in_page = SignInPage(page)
    request.cls.watchlist_page = WatchlistPage(page)
    request.cls.imdb_pro_page = ImdbProPage(page)
    request.cls.your_lists_page = YourListPage(page)
    request.cls.search_page = SearchPage(page)
    request.cls.video_page = VideoPage(page)
    request.cls.profile_page = ProfilePage(page)
    request.cls.your_ratings_page = YourRatingsPage(page)
    request.cls.your_watch_history_page = YourWatchHistoryPage(page)
    request.cls.account_settings_page = YourAccountSettingsPage(page)
    request.cls.advanced_search_page = AdvancedSearchPage(page)

    yield
    request.cls.page.close()
    #browser.close()


@pytest.fixture(scope="function")
def setup_page_function(request, browser):
    request.cls.page = browser.new_page()
    url = ConfigReader.read_config("global", "url")
    request.cls.page.goto(url)
    request.cls.main_page = MainPage(request.cls.page)
    request.cls.top_nav_bar = TopNavBar(request.cls.page)
    request.cls.sign_in_page = SignInPage(request.cls.page)
    request.cls.watchlist_page = WatchlistPage(request.cls.page)
    request.cls.imdb_pro_page = ImdbProPage(request.cls.page)
    request.cls.your_lists_page = YourListPage(request.cls.page)
    request.cls.search_page = SearchPage(request.cls.page)
    request.cls.video_page = VideoPage(request.cls.page)
    request.cls.profile_page = ProfilePage(request.cls.page)
    request.cls.your_ratings_page = YourRatingsPage(request.cls.page)
    request.cls.your_watch_history_page = YourWatchHistoryPage(request.cls.page)
    request.cls.account_settings_page = YourAccountSettingsPage(request.cls.page)
    request.cls.advanced_search_page = AdvancedSearchPage(request.cls.page)

    yield
    request.cls.page.close()
    browser.close()
