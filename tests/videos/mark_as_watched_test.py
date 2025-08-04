import time

import pytest
from tests.base_test import BaseTest

#  rate video
@pytest.mark.usefixtures("setup_page_class")

class TestMarkAsWatched(BaseTest):
    def test_add_to_watchlist(self):
        self.perform_login()
        #search for video
        self.top_nav_bar.search_category_and_name_click('Titles','the big bang theory')
        #click on "mark as watched btn"
        self.video_page.mark_as_watched()
        time.sleep(1)

        assert self.video_page.watched_btn_text() == 'Watched', 'Not as expected'

        self.video_page.mark_as_watched()


