from enum import StrEnum

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement

class ContextAlertMessage(StrEnum):
    ALERT_MSG = "You selected a context menu"

class ContextMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.context_area = WebElement(self.page.locator('//div[@id="hot-spot"]'),
                                       description='Context menu page -> context area with JS message')

    def click_on_context_area(self) -> str:
        return self.actions.run_and_accept_alert(self.context_area.right_click)
