import re

from pages.hover_page import HoverPage, HtmlAttributes

PATTERN = re.compile(f"^{HtmlAttributes.USERNAME}\d+")


def test_hover_page(page, base_url: str):
    hover_page = HoverPage(page)
    hover_page.action.goto(f"{base_url}/hovers")
    list_to_check = hover_page.get_user_names()

    for username in list_to_check:
        assert re.fullmatch(PATTERN, username) is not None, (
            f"Username {username} does not match name pattern: userN, where N - index number"
        )
