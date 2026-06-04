from random import choice

from playwright.sync_api import Page

from pages.slider_page import SliderPage


def test_slider(page: Page, base_url: str, endpoint):
    slider_page = SliderPage(page)
    slider_page.action.goto(f"{base_url}{endpoint[slider_page.__class__.__name__]}")
    slider_value = choice(slider_page.get_slider_values)
    num_of_press = int(slider_value * 2)
    slider_page.move_slider(num_of_press)
    actual_slider_value = slider_page.slider_value.get_inner_text()
    expected_slider_value = str(slider_value)
    assert str(expected_slider_value) == actual_slider_value, (
        f"Expected number {str(expected_slider_value)}, got {slider_page.slider_value}"
    )
