import time

import pytest
from tests.base_test import BaseTest

#creat new people list,
# add one person from search bar in list
# delete list
@pytest.mark.usefixtures("setup_page_class")

class TestAddActorTolist(BaseTest):
    def test_add_new_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new lis btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("My favorite actors", "Actors i like","People","Private")
        # add person
        self.your_lists_page.add_from_search_to_list('Robert Downey Jr')

        assert "Robert Downey Jr" in self.your_lists_page.people_title(), "Name not found"




