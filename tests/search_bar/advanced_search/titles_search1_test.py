import pytest
from tests.base_test import BaseTest

# search by titles
@pytest.mark.usefixtures("setup_page_class")

class TestTitlesSearch1(BaseTest):
    def test_titles_search1(self):
        # sign in
        self.perform_login()
        # go to advanced search
        self.top_nav_bar.advanced_search_btn()
        # title typs filter
        self.advanced_search_page.title_types('movie','tvSeries')
        # release date filter
        self.advanced_search_page.release_date('2021-01-01','2024-01-01')
        # imdb rating filter
        self.advanced_search_page.ratings('7','10')
        # gener filter
        self.advanced_search_page.genres('Action','Horror','Sci-Fi')
        # click on "see results" btn
        self.advanced_search_page.see_results_btn()

        # get selected filters from UI
        actual_filters = self.advanced_search_page.get_selected_filter_texts()
        # assert expected filters are in the list
        expected_filters = [
            "Movie",
            "TV Series",
            "Release Date",
            "Action",
            "Horror",
            "Sci-Fi",
            "IMDb ratings"
        ]
        for expected in expected_filters:
            assert any(expected in actual for actual in actual_filters), f"Missing filter: {expected}"

