from enum import IntEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderBoundaries(IntEnum):
    MIN = 1
    MAX = 9


class SliderPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
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
