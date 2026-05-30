from pages.slider_page import SliderPage


def test_slider(page, base_url, get_slider_value: int):
    slider_page = SliderPage(page)
    slider_page.action.goto(f"{base_url}/horizontal_slider")
    num_of_press, expected_slider_value = get_slider_value
    slider_page.move_slider(num_of_press)
    actual_slider_value = slider_page.slider_value.get_inner_text()
    assert expected_slider_value == actual_slider_value, \
        f"Expected number {expected_slider_value}, got {slider_page.slider_value}"
