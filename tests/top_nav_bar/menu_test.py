import pytest
from tests.base_test import BaseTest

#click on menu btn
@pytest.mark.usefixtures("setup_page_class")
class TestMenu(BaseTest):
    def test_menu(self):
        self.main_page.menu_btn()

        assert self.main_page.menu(), "Drawer menu did not open as expected"