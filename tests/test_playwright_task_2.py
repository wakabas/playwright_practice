import pytest

from models.pages.main_page import MainPage
from models.pages.search_result_page import Options

keywords = ["city", "habits"]
num_of_articles = [10, 15]
filter_types = [Options.ASC, Options.DESC]


@pytest.mark.parametrize("filter_type", filter_types)
@pytest.mark.parametrize("n", num_of_articles)
@pytest.mark.parametrize("name", keywords)
def test_search_page(name: str, n: int, filter_type: Options, page, url):
    main_page = MainPage(page)
    main_page.page.goto(url)
    search_page = main_page.search_articles(name)
    search_page.sort_by_filter(filter_type)
    price_list = search_page.get_article_prices(n)
    match filter_type:
        case Options.ASC:
            assert price_list == sorted(price_list), f"Sort filter does not match {filter_type}"
        case Options.DESC:
            assert price_list == sorted(price_list, reverse=True), f"Sort filter does not match {filter_type}"
