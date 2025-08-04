
import pytest
from tests.base_test import BaseTest

#creat new video watchlist,
# add one video from search bar in watchlist
# delete list
@pytest.mark.usefixtures("setup_page_class")

class TestAddVideosToWatchlist(BaseTest):
    def test_add_new_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new lis btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("My best movies", "My top movie, picks I can watch again and again","Videos","Private")
        # add link video
        self.your_lists_page.add_link_to_list('https://www.imdb.com/video/vi4260218905/?ref_=ttvg_vi_1')


        assert any("Untamed" in title for title in self.your_lists_page.movie_titles()), "Movie title not found"



