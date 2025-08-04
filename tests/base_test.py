from pages.account_settings_page import YourAccountSettingsPage
from pages.advanced_search_page import AdvancedSearchPage
from pages.imbd_pro_page import ImdbProPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.search_page import SearchPage
from pages.sign_in_page import SignInPage
from pages.top_nav_bar import TopNavBar
from pages.video_page import VideoPage
from pages.watchlist_page import WatchlistPage
from pages.your_lists_page import YourListPage
from pages.your_ratings_page import YourRatingsPage
from pages.your_watch_history_page import YourWatchHistoryPage
from playwright.sync_api import Page
from utils.config_reader import ConfigReader

class BaseTest:
    page: Page
    main_page: MainPage
    top_nav_bar: TopNavBar
    sign_in_page: SignInPage
    watchlist_page: WatchlistPage
    imdb_pro_page: ImdbProPage
    your_lists_page: YourListPage
    search_page: SearchPage
    video_page: VideoPage
    profile_page: ProfilePage
    your_ratings_page: YourRatingsPage
    your_watch_history_page: YourWatchHistoryPage
    account_settings_page: YourAccountSettingsPage
    advanced_search_page: AdvancedSearchPage

    def perform_login(self):
        self.main_page.sign_in_btn()
        email = ConfigReader.read_config("user", "user")
        password = ConfigReader.read_config("user", "password")
        self.sign_in_page.sign_in_imdb(email, password)