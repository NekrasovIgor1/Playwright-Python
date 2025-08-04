import pytest
from tests.base_test import BaseTest

# search by all category
@pytest.mark.usefixtures("setup_page_class")

class TestSearchByAllCategory(BaseTest):
    def test_search_by_all_category(self):
        self.perform_login()
        # search by all category
        category_text = 'All'
        search_text = "the terminator"
        self.top_nav_bar.search_by_category_and_name(category_text, search_text)

        # Assertions
        header = self.search_page .get_header_text()
        category = self.search_page.get_category_text()
        first_result = self.search_page.get_first_result_text()

        # verify that the search text appears in the header (case-insensitive)
        assert search_text.lower() in header.lower(), f"Expected '{search_text}' in header, but got '{header}'"
        # verify that the selected search category is 'all'
        assert category == 'Titles', f"Expected category 'Titles', but got '{category}'"
        # verify that the first search result contains the search text (case-insensitive)
        assert search_text.lower() in first_result.lower(), f"Expected '{search_text}' in first result, but got '{first_result}'"

