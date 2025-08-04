import pytest
from tests.base_test import BaseTest

# profile menu links check
@pytest.mark.usefixtures("setup_page_class")

class TestYourProfile(BaseTest):
    def test_your_profile(self):
        # perform log in
        self.perform_login()
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('your_profile')

        assert 'Welcome to your new profile' == self.profile_page.legacy_alert(), 'Not as expected'

    def test_your_watchlist(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('your_watchlist')

        assert 'Your Watchlist' == self.watchlist_page.page_header(), 'Not as expected'

    def test_your_ratings(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('your_ratings')

        assert 'Your ratings' == self.your_ratings_page.page_header(), 'Not as expected'

    def test_your_list(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('your_lists')

        assert 'Your lists' == self.your_lists_page.page_header(), 'Not as expected'

    def test_your_watch_history(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('your_watch_history')

        assert 'Your watch history' == self.your_watch_history_page.page_header(), 'Not as expected'

    def test_account_settings(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('account_settings')

        assert 'Account settings' == self.account_settings_page.page_header(), 'Not as expected'

    def test_sing_out(self):
        # click on profile btn
        self.top_nav_bar.profile_btn()
        # click on "your profile"
        self.top_nav_bar.click_user_menu_item('sign_out')

        expected_url = 'https://www.imdb.com/registration/signin/?u=%2Fregistration%2Faccountsettings%2F&ref_=acset'
        current_url = self.page.url
        # assert current URL matches expected
        assert current_url == expected_url, f"Expected URL '{expected_url}', but got '{current_url}'"





