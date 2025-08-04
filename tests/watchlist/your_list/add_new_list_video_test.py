import time

import pytest
from tests.base_test import BaseTest

#creat new list video tipe
@pytest.mark.usefixtures("setup_page_class")

class TestAddNewListVideo(BaseTest):
    def test_add_new_list_video(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # click on create new lis btn
        self.watchlist_page.create_new_list("Movies", "My top movie picks I can watch again and again","Videos","Private")

        actual_title = self.your_lists_page.page_header()
        assert actual_title == "Movies", f"Expected title 'Movies', but got '{actual_title}'"



