import time

from playwright.sync_api import Page

class BasePage:
    def __init__(self,page: Page):
        self.__page = page

    def click (self, locator):
        self._highlight_element(locator, "green")
        self.__page.locator(locator).click()

    def click_inside(self, parent_locator, child_selector):
        self._highlight_element(parent_locator, "green")
        parent_locator.locator(child_selector).click()

    def check(self, locator):
        self._highlight_element(locator, "green")
        self.__page.locator(locator).check()

    def check_inside(self, parent_locator, child_selector):
        self._highlight_element(parent_locator, "green")
        parent_locator.locator(child_selector).check()

    def fill_text (self,locator,text):
        self._highlight_element(locator, "green")
        self.__page.locator(locator).fill(text)

    def inner_text(self,locator):
        return self.__page.locator(locator).inner_text()

    def get_locator(self, selector: str):
        time.sleep(1)
        return self.__page.locator(selector)

    def get_text(self, selector: str) -> str:
        return self.__page.locator(selector).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.__page.locator(locator).is_visible()

    def wait_for_locator(self, locator: str, timeout: int = 60000):
        self.__page.wait_for_selector(locator, state='visible', timeout=timeout)

    def wait_for_url(self, url: str, timeout: int = 60000):
        self.__page.wait_for_url(url, timeout=timeout)

    def scroll_by_pixels(self, pixels: int):
        self.__page.evaluate(f"window.scrollBy(0, {pixels})")

    def evaluate_script(self, script: str):
        self.__page.evaluate(script)

    def reload_page(self):
        self.__page.reload()


    # Highlights a web element temporarily by changing its background color and box shadow.
    # This is useful for debugging or visual tracking during automated test runs.
    # Parameters:
    #   locator (str): The selector used to locate the element on the page.
    #   color (str): The background color to use for highlighting (default is yellow).
    def _highlight_element(self, locator, color: str = "yellow"):
        # If the locator is a string – convert it to a Locator
        if isinstance(locator, str):
            locator = self.__page.locator(locator)

        locator.evaluate(f"""
            (el) => {{
                const origShadow = el.style.boxShadow;
                const origBackground = el.style.backgroundColor;

                el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
                el.style.backgroundColor = '{color}';

                setTimeout(() => {{
                    el.style.boxShadow = origShadow;
                    el.style.backgroundColor = origBackground;
                }}, 300);
            }}
        """)
