import time

import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_class")

class TestDeleteList(BaseTest):
    def test_delete_list(self):
        self.perform_login()
        # click on watchlist btn
        self.main_page.watchlist_btn()
        # create new list
        self.watchlist_page.create_new_list('Want to watch','movies is want to watch','Videos','Public')
        # click on your list btn
        self.watchlist_page.your_list_btn()
        time.sleep(2)
        # delete list by name
        self.your_lists_page.delete_list('Want to watch')

        assert not  self.your_lists_page.is_list_exist("Want to watch"), "The list still exists after deletion"
