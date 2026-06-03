from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class ContextAlertMessage(StrEnum):
    ALERT_MSG = "You selected a context menu"


class ContextMenuPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.context_area = WebElement(
            self.page.locator('//div[@id="hot-spot"]'),
            description="Context menu page -> context area with JS message",
        )

    def click_on_context_area(self) -> str:
        return self.action.run_and_accept_alert(self.context_area.right_click)
