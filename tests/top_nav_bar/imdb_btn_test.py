import pytest
from tests.base_test import BaseTest

@pytest.mark.usefixtures("setup_page_class")

# click on banner icon
class TestImdbBtn(BaseTest):
    def test_imdb_btn(self):
        self.main_page.banner_btn()

        assert self.page.url == "https://www.imdb.com/?ref_=hm_nv_home"

