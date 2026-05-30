from enum import StrEnum

from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertMessages(StrEnum):
    ALERT_MSG = "I am a JS Alert"
    CONFIRM_MSG = "I am a JS Confirm"
    PROMPT_MSG = "I am a JS prompt"


class ResultMessages(StrEnum):
    ALERT_RESULT = "You successfully clicked an alert"
    CONFIRM_RESULT_OK = "You clicked: Ok"
    PROMPT_RESULT = "You entered: "


class AlertPage:
    def __init__(self, page: Page):
        self.page = page
        self.action = PageActions(self.page)
        self.alert_btn = WebElement(
            self.page.get_by_role("button", name="Click for JS Alert"),
            description="Alert page -> JS alert button",
        )
        self.confirm_btn = WebElement(
            self.page.get_by_role("button", name="Click for JS Confirm"),
            description="Alert page -> JS confirm button",
        )
        self.prompt_btn = WebElement(
            self.page.get_by_role("button", name="Click for JS Prompt"),
            description="Alert page -> JS prompt button",
        )
        self.result_text = WebElement(
            self.page.locator(
                '//p[@id="result" and starts-with(normalize-space(.), "You")]'
            ),
            description="Alert page -> JS alert result text",
        )

    def receive_msg_from_alert_btn(self) -> str:
        return self.action.run_and_accept_alert(self.alert_btn.click)

    def receive_msg_from_confirm_btn(self) -> str:
        return self.action.run_and_accept_alert(self.confirm_btn.click)

    def receive_msg_from_prompt_btn(self, text: str) -> str:
        return self.action.run_and_accept_prompt(self.prompt_btn.click, text)
