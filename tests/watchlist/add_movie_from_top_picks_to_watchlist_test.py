import time

import pytest
from tests.base_test import BaseTest

# add video from main page - "top picks on imdb this week" section ,to watchlist
@pytest.mark.usefixtures("setup_page_class")

class TestAddMovieFromTopPicksToWatchlist(BaseTest):
    def test_add_movie_from_top_picks_to_watchlist(self):
        self.perform_login()
        # add the first movie (index 1) from the Top picks section to the watchlist,
        # and get the movie title for validation
        movie_name_added = self.main_page.add_movie_to_watchlist_by_index_from_top_picks(4)
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # get the list of all movie titles currently displayed in the Watchlist
        movie_titles = self.watchlist_page.get_watchlist_titles()
        # verify that the movie added is present in the Watchlist
        assert movie_name_added in movie_titles, f"Movie '{movie_name_added}' not found in the watchlist."




