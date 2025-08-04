

import pytest
from tests.base_test import BaseTest


# create new titles list,
# add 2 movies from search bar to list
# delete one movie from list
# delete list
@pytest.mark.usefixtures("setup_page_class")
class TestCopyMovieToWatchlist(BaseTest):
    def test_copy_movie_to_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new list btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("movies to watch with my wife", "wife movies", "Titles", "Private")
        # add movie
        self.your_lists_page.add_from_search_to_list('Game of Thrones')
        # select movie to delete
        self.your_lists_page.select_movie_for_delete('Game of Thrones', 'Your Watchlist')

        assert any('Game of Thrones' not in title for title in self.your_lists_page.movie_titles()), "Game of Thrones' still appears in the list after being moved."











