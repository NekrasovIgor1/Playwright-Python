import pytest
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader

@pytest.mark.usefixtures("setup_page_class")
class TestSignIn(BaseTest):
    def test_sign_in(self):
        self.perform_login()

        # verify username is shown after login
        username_text = self.top_nav_bar.get_tex_profile_name()
        assert "igor" in username_text
