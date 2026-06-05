from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class ButtonText(StrEnum):
    JS_ALERT = "Click for JS Alert"
    JS_CONFIRM = "Click for JS Confirm"
    JS_PROMPT = "Click for JS Prompt"


class AlertMessages(StrEnum):
    ALERT_MSG = "I am a JS Alert"
    CONFIRM_MSG = "I am a JS Confirm"
    PROMPT_MSG = "I am a JS prompt"


class ResultMessages(StrEnum):
    ALERT_RESULT = "You successfully clicked an alert"
    CONFIRM_RESULT_OK = "You clicked: Ok"
    PROMPT_RESULT = "You entered: "


class AlertPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.alert_btn = WebElement(
            self.page.get_by_role("button", name=ButtonText.JS_ALERT),
            description="Alert page -> JS alert button",
        )
        self.confirm_btn = WebElement(
            self.page.get_by_role("button", name=ButtonText.JS_CONFIRM),
            description="Alert page -> JS confirm button",
        )
        self.prompt_btn = WebElement(
            self.page.get_by_role("button", name=ButtonText.JS_PROMPT),
            description="Alert page -> JS prompt button",
        )
        self.result_text = WebElement(
            self.page.locator('//*[@id="result"]'),
            description="Alert page -> JS alert result text",
        )

    def receive_msg_from_alert_btn(self) -> str:
        return self.action.run_and_accept_alert(self.alert_btn.click)

    def receive_msg_from_confirm_btn(self) -> str:
        return self.action.run_and_accept_alert(self.confirm_btn.click)

    def receive_msg_from_prompt_btn(self, text: str) -> str:
        return self.action.run_and_accept_prompt(self.prompt_btn.click, text)
