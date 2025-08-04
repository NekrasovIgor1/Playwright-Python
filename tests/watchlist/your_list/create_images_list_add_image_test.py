import time

import pytest
from tests.base_test import BaseTest

#creat new Images list,
# add one Image from link bar in list
# delete list
@pytest.mark.usefixtures("setup_page_class")

class TestAddImageTolist(BaseTest):
    def test_add_new_watchlist(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new lis btn
        self.watchlist_page.create_new_list_btn()
        # fill in info
        self.watchlist_page.fill_info("My favorite images", "My best Images","Images","Private")
        # add link image
        self.your_lists_page.add_link_to_list('https://www.imdb.com/title/tt1757678/mediaviewer/rm2303311106/?ref_=tt_ov_i')

        assert "Oona Chaplin" in self.your_lists_page.image_title(), "Image title not found"




