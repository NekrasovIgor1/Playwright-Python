from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class SignInPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


    __SIGN_IN_WITH_IMDB = 'div:nth-child(2) > a:nth-child(3)'
    __EMAIL = '#ap_email'
    __PASSWORD = '#ap_password'
    __SIGN_IN_BTN = '#signInSubmit'
    __REMEMBER_ME_CHECKBOX = "[name='rememberMe']"

    def sign_in_with_imdb_btn(self):
        self.click(self.__SIGN_IN_WITH_IMDB)

        #fill info in sign in page
    def fill_info(self,email, password):
        self.fill_text(self.__EMAIL, email)
        self.fill_text(self.__PASSWORD, password)
        self.check(self.__REMEMBER_ME_CHECKBOX)
        self.click(self.__SIGN_IN_BTN)

        #sign in with imdb account and fill info
    def sign_in_imdb(self, email: str, password: str):
        self.sign_in_with_imdb_btn()
        self.fill_info(email, password)
        time.sleep(5)
        #self.wait_for_url("https://www.imdb.com/")

        # sign in with imdb account and fill negative info
    def sign_in_imdb_negative(self, email: str, password: str):
        self.sign_in_with_imdb_btn()
        self.fill_info(email, password)

    def fill_info_negative_test(self,email,password):
        self.fill_info(email, password)

        #get error message when no password entered
    def error_message_no_password(self):
        return self.inner_text('#auth-password-missing-alert > div')

        # get error message when no email entered
    def error_message_no_email(self):
        return self.inner_text('#auth-email-missing-alert > div')

        # get error message when wrong email or password is entered
    def error_message_wrong_email_or_password(self):
        return self.inner_text('#auth-error-message-box')










