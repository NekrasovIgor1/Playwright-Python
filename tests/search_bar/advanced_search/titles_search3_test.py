import time

import pytest
from tests.base_test import BaseTest


# search by titles
@pytest.mark.usefixtures("setup_page_class")
class TestTitlesSearch3(BaseTest):
    def test_titles_search3(self):
        # sign in
        self.perform_login()
        # go to advanced search
        self.top_nav_bar.advanced_search_btn()
        # title typs filter
        self.advanced_search_page.title_types('tvShort')
        # release date filter
        self.advanced_search_page.release_date('2000-01-01', '2025-01-01')
        # imdb rating filter
        self.advanced_search_page.ratings('6', '')
        # gener filter
        self.advanced_search_page.genres('Drama', 'Animation','Film-Noir')
        # click on "see results" btn
        self.advanced_search_page.see_results_btn()

        # get selected filters from UI
        actual_filters = self.advanced_search_page.get_selected_filter_texts()
        # assert expected filters are in the list
        expected_filters = [
            "TV Short",
            "Release Date",
            "Drama",
            "Animation",
            "Film-Noir",
            "IMDb ratings"
        ]
        for expected in expected_filters:
            assert any(expected in actual for actual in actual_filters), f"Missing filter: {expected}"

