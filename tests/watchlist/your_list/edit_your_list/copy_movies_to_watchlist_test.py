import time

import pytest
from tests.base_test import BaseTest


# create new titles list,
# add 1 movie from search bar to list
# copy movie to watchlist
# delete all lists
@pytest.mark.usefixtures("setup_page_class")
class TestCopyMovieToWatchlist(BaseTest):
    def test_copy_movie_to_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new list btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("My top movies", "My best movies", "Titles", "Private")
        # add movie
        self.your_lists_page.add_from_search_to_list('Armageddon')
        # select movie to copy
        self.your_lists_page.select_movie_for_copy('Armageddon', 'Your Watchlist')

        movie_titles = self.your_lists_page.movie_titles()
        assert any('Armageddon' in title for title in movie_titles), \
            "Movie 'Armageddon' not appears in the list after being copied."

        # Go to watchlist and check if the movie added
        self.main_page.watchlist_btn()

        movie_titles = self.watchlist_page.movie_titles()
        assert 'Armageddon' in movie_titles, "Movie 'Armageddon' not found in the new list."











