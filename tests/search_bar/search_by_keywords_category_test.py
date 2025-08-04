
import pytest
from tests.base_test import BaseTest

# search by keywords category
@pytest.mark.usefixtures("setup_page_class")

class TestSearchByKeywordsCategory(BaseTest):
    def test_search_by_keywords_category(self):
        self.perform_login()
        # search by keywords category
        category_text = 'Keywords'
        search_text = "agriculture"
        self.top_nav_bar.search_by_category_and_name(category_text, search_text)

        # Assertions
        header = self.search_page .get_header_text()
        category = self.search_page.get_category_text()
        first_result = self.search_page.get_first_result_text()

        # verify that the search text appears in the header (case-insensitive)
        assert search_text.lower() in header.lower(), f"Expected '{search_text}' in header, but got '{header}'"
        # verify that the selected search category is 'keywords'
        assert category_text == category, f"Expected category '{category_text}', but got '{category}'"
        # verify that the first search result contains the search text (case-insensitive)
        assert search_text.lower() in first_result.lower(), f"Expected '{search_text}' in first result, but got '{first_result}'"

