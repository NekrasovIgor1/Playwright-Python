import pytest
from tests.base_test import BaseTest

#  rate video
@pytest.mark.usefixtures("setup_page_class")

class TestAddToWatchList(BaseTest):
    def test_add_to_watchlist(self):
        # perform log in
        self.perform_login()
        #search for video
        self.top_nav_bar.search_category_and_name_click('Titles','how i met you mother')
        # add video to watchlist
        self.video_page.add_to_watchlist_btn()

        assert self.video_page.is_watchlist_checked(), "Expected item to be in watchlist (checked)"
        assert self.video_page.is_watchlist_text_in(), "Expected 'In Watchlist' text on button"
        assert self.video_page.is_poster_v_visible(), "Expected V ribbon icon to be visible on thumbnail"



