import re

from pages.hover_page import HoverPage, HtmlAttributes
from ui.page_actions import PageActions

PATTERN = re.compile(f"^{HtmlAttributes.USERNAME}\d+")


def test_hover_page(page, base_url: str):
    tmp_page = PageActions(page)
    tmp_page.goto(f"{base_url}/hovers")
    hover_page = HoverPage(tmp_page.page)
    list_to_check = hover_page.get_user_names()

    for username in list_to_check:
        assert re.fullmatch(PATTERN, username) is not None, (
            f"Username {username} does not match pattern name: userN, where N - index number"
        )
