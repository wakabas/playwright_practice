from enum import StrEnum

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class SuccessMessage(StrEnum):
    MESSAGE = "Congratulations! You must have the proper credentials."


class BasicAuthPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.success_text = WebElement(
            self.page.get_by_text(SuccessMessage.MESSAGE),
            description="Basic auth page -> Success message",
        )
        self.action = PageActions(self.page)
