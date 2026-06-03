from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class NameAttrText(StrEnum):
    NEW_WINDOW_LINK = "Click Here"
    NEW_WINDOW_TEXT = "New Window"


class MainWindowPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.new_window_href = WebElement(
            self.page.get_by_role("link", name=NameAttrText.NEW_WINDOW_LINK),
            description="Main window page -> href for new page",
        )

    def switch_to_new_window(self) -> "NewWindowPage":
        with self.action.expect_new_page() as new_page_info:
            self.new_window_href.click()
            new_page = NewWindowPage(new_page_info.value)
            new_page.action.bring_to_front()
            return new_page


class NewWindowPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.text = WebElement(
            self.page.get_by_role("heading", name=NameAttrText.NEW_WINDOW_TEXT),
            description="New window page -> text for check",
        )

    def get_new_window_text(self) -> str:
        return self.text.get_inner_text()