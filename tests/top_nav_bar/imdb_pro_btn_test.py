import pytest
from tests.base_test import BaseTest

#click on imdb pro banner
@pytest.mark.usefixtures("setup_page_class")

class TestImdbProBtn(BaseTest):
    def test_imdb_pro_btn(self):
        self.main_page.imdbpro_btn()

        message_text = self.imdb_pro_page.message_text()
        assert message_text == 'Get the essential resource for entertainment professionals'




