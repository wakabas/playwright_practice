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
            self.page.locator("//div[contains(@class, jscroll-added)]/child::br"),
            description="Infinite scroll page -> paragraph",
        )

    def scroll_until(self):
        while self.paragraph.count() < NumberOfParagraphs.MIN:
            self.action.scroll_page_down()
            self.page.wait_for_timeout(1000)
