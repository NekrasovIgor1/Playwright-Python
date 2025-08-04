from playwright.sync_api import Page
from pages.base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __LEGACY_ALERT  = '[data-testid="user-legacy-alert"] > div >div'

    def legacy_alert(self):
       return self.get_text(self.__LEGACY_ALERT)