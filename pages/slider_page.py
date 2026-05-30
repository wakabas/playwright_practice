from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.action = PageActions(self.page)
        self.slider = WebElement(
            self.page.locator("//input[@type='range']").and_(
                self.page.get_by_role("slider")
            ),
            description="Slider page -> slider",
        )
        self.slider_value = WebElement(
            self.page.locator("//span[@id='range']"),
            description="Slider page -> slider numeric value",
        )

    def move_slider(self, value: int) -> None:
        self.slider.focus()
        self.slider.press("+".join(["ArrowRight"] * value))
