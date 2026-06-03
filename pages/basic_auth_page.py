from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SuccessMessage(StrEnum):
    MESSAGE = "Congratulations! You must have the proper credentials."


class BasicAuthPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.success_text = WebElement(
            self.page.get_by_text(SuccessMessage.MESSAGE),
            description="Basic auth page -> Success message",
        )
