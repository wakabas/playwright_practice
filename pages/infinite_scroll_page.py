import time
from enum import IntEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class NumberOfParagraphs(IntEnum):
    MIN = 10


class InfiniteScrollPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.paragraph = MultiWebElement(
            self.page.locator("//*[contains(@class, jscroll-added)]//br"),
            description="Infinite scroll page -> paragraph",
        )

    def scroll_until(self, timeout: int = 10, poll_interval: float = 0.5):
        start = time.time()
        while True:
            if self.paragraph.count() >= NumberOfParagraphs.MIN:
                break

            self.action.scroll_page_down()

            if time.time() - start > timeout:
                raise TimeoutError("Параграф не появился за отведенное время")

            time.sleep(poll_interval)
