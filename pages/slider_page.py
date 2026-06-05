from enum import IntEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SliderPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.slider = WebElement(
            self.page.locator("//*[@type='range']").and_(
                self.page.get_by_role("slider")
            ),
            description="Slider page -> slider",
        )
        self.slider_value = WebElement(
            self.page.locator("//*[@id='range']"),
            description="Slider page -> slider numeric value",
        )

    @property
    def slider_values(self):
        slider_min = int(float(self.slider.get_attribute("min")))
        slider_max = int(float(self.slider.get_attribute("max")))
        slider_step = float(self.slider.get_attribute("step"))
        return [
            (num + slider_step)
            for num in range(slider_max)
            if (num + slider_step) < slider_max
        ]

    def move_slider(self, value: int) -> None:
        self.slider.focus()
        self.slider.press("+".join(["ArrowRight"] * value))
