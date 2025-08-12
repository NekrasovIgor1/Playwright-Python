import pytest
from tests.base_test import BaseTest


@pytest.mark.usefixtures("setup_page_class")

class TestSignInNegative(BaseTest):
        #corect email, no password
    def test_sign_in_negative_no_password(self):
        self.main_page.sign_in_btn()
        self.sign_in_page.sign_in_imdb_negative('nekrasovigor1@gmail.com','')

        error_text = self.sign_in_page.error_message_no_password()
        assert "Enter your password" in error_text

        #no email, correct password
    def test_sign_in_negative_no_email(self):
        self.sign_in_page.fill_info_negative_test('', 'nekrasovigor1')

        error_text = self.sign_in_page.error_message_no_email()
        assert "Enter your email or mobile phone number" in error_text

        #wrong email, correct password
     def test_sign_in_negative_wrong_email(self):
         self.sign_in_page.fill_info_negative_test('nekrasovigor2@gmail.com', 'nekrasovigor1')
    
         error_text = self.sign_in_page.error_message_wrong_email_or_password()
         assert "We cannot find an account with that email address" in error_text
    
         # correct email, wrong password
     def test_sign_in_negative_wrong_password(self):
         self.sign_in_page.fill_info_negative_test('nekrasovigor1@gmail.com', 'nekrasovigor')
    
         error_text = self.sign_in_page.error_message_wrong_email_or_password()
         assert "Your password is incorrect" in error_text








