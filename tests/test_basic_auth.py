from pages.basic_auth_page import BasicAuthPage, SuccessMessage
from utils.url_utils import embed_credentials_in_url


def test_basic_auth(page, basic_auth_url):
    basic_auth_page = BasicAuthPage(page)
    auth_url = embed_credentials_in_url(**basic_auth_url)
    basic_auth_page.action.goto(auth_url)
    received_text = basic_auth_page.success_text.get_inner_text()

    assert received_text == SuccessMessage.MESSAGE, (
        f"Expected message - {SuccessMessage.MESSAGE}, received message - {received_text}"
    )
