import time

import pytest
from tests.base_test import BaseTest


# search by titles
@pytest.mark.usefixtures("setup_page_class")
class TestTitlesSearch2(BaseTest):
    def test_titles_search2(self):
        # sign in
        self.perform_login()
        # go to advanced search
        self.top_nav_bar.advanced_search_btn()
        # title typs filter
        self.advanced_search_page.title_types('tvSeries','video')
        # release date filter
        self.advanced_search_page.release_date('2010-01-01', '2020-01-01')
        # imdb rating filter
        self.advanced_search_page.ratings('9', '')
        # gener filter
        self.advanced_search_page.genres('Drama', 'Fantasy')
        # click on "see results" btn
        self.advanced_search_page.see_results_btn()

        # get selected filters from UI
        actual_filters = self.advanced_search_page.get_selected_filter_texts()
        # assert expected filters are in the list
        expected_filters = [
            "TV Series",
            "Video",
            "Release Date",
            "Drama",
            "Fantasy",
            "IMDb ratings"
        ]
        for expected in expected_filters:
            assert any(expected in actual for actual in actual_filters), f"Missing filter: {expected}"

