import pytest

from models.pages.main_page import MainPage
from models.pages.search_result_page import Options

test_data = [
    ("city", 10, Options.ASC),
    ("city", 15, Options.DESC),
    ("habits", 10, Options.ASC),
    ("habits", 15, Options.DESC),
]


@pytest.mark.parametrize(
    "name, n, filter_type",
    test_data,
)
def test_search_page(name: str, n: int, filter_type: str, page, url):
    main_page = MainPage(page)
    main_page.page.goto(url)
    search_page = main_page.search_articles(name)
    search_page.sort_by_filter(filter_type)
    price_list = search_page.get_article_prices(n)
    match filter_type:
        case Options.ASC:
            assert all(
                current_num <= next_num
                for current_num, next_num in zip(price_list, price_list[1:])
            )
        case Options.DESC:
            assert all(
                current_num >= next_num
                for current_num, next_num in zip(price_list, price_list[1:])
            )
