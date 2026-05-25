import pytest

from models.pages.main_page import MainPage
from models.pages.search_result_page import Options

keywords = ["city", "habits"]
num_and_filter_types = [(10, Options.ASC), (15, Options.DESC)]


@pytest.mark.parametrize("n, filter_type", num_and_filter_types)
@pytest.mark.parametrize("name", keywords)
def test_search_page(name: str, n: int, filter_type: Options, page, url):
    main_page = MainPage(page)
    main_page.page.goto(url)
    search_page = main_page.search_articles(name)
    search_page.sort_by_filter(filter_type)
    received_price_list = search_page.get_article_prices(n)
    match filter_type:
        case Options.ASC:
            expected_price_list = sorted(received_price_list)
            assert received_price_list == expected_price_list, \
                f"Expected: {expected_price_list}, received: {received_price_list}"
        case Options.DESC:
            expected_price_list = sorted(received_price_list, reverse=True)
            assert received_price_list == expected_price_list, \
                f"Expected: {expected_price_list}, received: {received_price_list}"
