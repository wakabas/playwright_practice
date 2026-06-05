from playwright.sync_api import Page

from pages.infinite_scroll_page import InfiniteScrollPage, NumberOfParagraphs


def test_infinite_scroll(page: Page, base_url: str, endpoint):
    infinite_scroll_page = InfiniteScrollPage(page)
    infinite_scroll_page.action.goto(f"{base_url}{endpoint[infinite_scroll_page.__class__.__name__]}")
    infinite_scroll_page.scroll_until()
    count_of_paragraphs = infinite_scroll_page.paragraph.count()
    assert count_of_paragraphs >= NumberOfParagraphs.MIN, (
        f"Expected count of paragraphs >= {NumberOfParagraphs.MIN}, but got {count_of_paragraphs}"
    )
