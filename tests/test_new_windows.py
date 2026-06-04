from playwright.sync_api import Page

from pages.new_window_page import MainWindowPage, NameAttrText, NewWindowPage


def verify_text(sub_page: NewWindowPage):
    actual_text = sub_page.get_new_window_text()
    assert actual_text == NameAttrText.NEW_WINDOW_TEXT, (
        f"Expected text - {NameAttrText.NEW_WINDOW_TEXT}, but got {actual_text}"
    )


def test_new_window_page(page: Page, base_url: str, endpoint):
    main_page = MainWindowPage(page)
    main_page.action.goto(f"{base_url}{endpoint[main_page.__class__.__name__]}")
    sub_page_1 = main_page.switch_to_new_window()
    verify_text(sub_page_1)
    sub_page_2 = main_page.switch_to_new_window()
    verify_text(sub_page_2)
    sub_page_1.action.close_page()
    sub_page_2.action.close_page()
    num_of_pages = main_page.action.get_number_of_pages()
    assert num_of_pages == 1, f"Expected number of pages - 1, but got {num_of_pages}"
