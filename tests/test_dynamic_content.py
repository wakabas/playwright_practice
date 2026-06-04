from playwright.sync_api import Page

from pages.dynamic_content_page import DynamicContentPage, NumOfOriginalAvatar


def test_dynamic_content(page: Page, base_url: str, endpoint):
    dynamic_page = DynamicContentPage(page)
    dynamic_page.action.goto(f"{base_url}{endpoint[dynamic_page.__class__.__name__]}")
    num_of_original_avatars = dynamic_page.wait_for_unique_avatars()
    assert num_of_original_avatars <= NumOfOriginalAvatar.MIN, (
        f"Expected count of original avatars is lesser than {NumOfOriginalAvatar.MIN}, but got {num_of_original_avatars}"
    )
