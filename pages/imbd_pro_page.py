from playwright.sync_api import Page
from pages.base_page import BasePage

class ImdbProPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __MESSAGE_TEXT = '#pro_login_box > div > h2'

    def message_text(self):
        return self.get_text(self.__MESSAGE_TEXT)

