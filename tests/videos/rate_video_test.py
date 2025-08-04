import pytest
from tests.base_test import BaseTest

#  rate video
@pytest.mark.usefixtures("setup_page_class")

class TestRateVideo(BaseTest):
    def test_rate_video(self):
        self.perform_login()
        #search for video
        self.top_nav_bar.search_category_and_name_click('Titles','Fantastic Four')
        # click on rate btn
        self.video_page.rate_btn_click()
        # rate video for 6 stars and click "rate" confirm btn
        stars_amount = '6'
        self.video_page.rate_stars(stars_amount)

        actual_rate:int = self.video_page.get_your_ratings()
        assert stars_amount == actual_rate, f"Expected '{stars_amount}' in header, but got '{actual_rate}'"

        self.video_page.rate_btn_click()
        self.video_page.remove_ratings()



