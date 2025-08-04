import time
from time import sleep

import pytest
from tests.base_test import BaseTest


# create new titles list,
# add 2 movie from search bar to list
# move movie to watchlist list
# delete all lists
@pytest.mark.usefixtures("setup_page_class")
class TestTransferMovieToWatchlist(BaseTest):
    def test_transfer_movie_to_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new list btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("My top movies", "My best movies", "Titles", "Private")
        # add movies
        self.your_lists_page.add_from_search_to_list('Beetlejuice Beetlejuice 2024')
        self.your_lists_page.add_from_search_to_list('Robert Downey Jr: High Altitude')
        # select movie to move
        self.your_lists_page.select_movie_for_move('Beetlejuice Beetlejuice', 'Your Watchlist')


        movie_titles = self.your_lists_page.movie_titles()
        assert 'Beetlejuice Beetlejuice' not in movie_titles, "Movie 'Beetlejuice Beetlejuice' still appears in the list after being moved."

        # Go to watchlist and check if the movie added
        self.main_page.watchlist_btn()


        movie_titles = self.watchlist_page.movie_titles()
        assert 'Beetlejuice Beetlejuice' in movie_titles, "Movie 'Beetlejuice Beetlejuice' not found in the new list."










