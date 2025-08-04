import time

import pytest
from tests.base_test import BaseTest

#creat new titles list,
# add one movie from search bar in list
# delete list
@pytest.mark.usefixtures("setup_page_class")

class TestCreateTitlesListAddVideo(BaseTest):
    def test_create_titles_list_add_video(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new lis btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info('Top 10', "Top 10 movies for 2024","Titles","Private")
        # add movie
        self.your_lists_page.add_from_search_to_list('The Hunting Wives')
        time.sleep(3)


        assert "The Hunting Wives" in self.your_lists_page.movie_titles(), "Name not found"




