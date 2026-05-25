from enum import StrEnum

from playwright.sync_api import Locator


class Options(StrEnum):
    ASC = "price_asc"
    DESC = "price_desc"


class SearchResultPage:
    def __init__(self, page):
        self.page = page
        self.results_loader = page.get_by_test_id("results-loader-svg")
        self.sort_list = page.get_by_test_id("filter-sort")
        self.apply_button = page.get_by_test_id("apply-filters-button")
        self.list_of_prices = self.page.locator(
            "[data-testid^='search-result-price-']"
        ).all()

    def wait_for_load(self):
        self.results_loader.wait_for(state="visible")
        self.results_loader.wait_for(state="hidden")

    def sort_by_filter(self, filter_type: Options):
        self.sort_list.click()
        self.sort_list.select_option(value=filter_type)
        self.apply_button.click()
        self.wait_for_load()

    @staticmethod
    def _parse_price(price: Locator) -> int:
        return int(price.inner_text().split(maxsplit=1)[0])

    def get_article_prices(self, num_of_articles: int) -> list[int]:
        article_to_parse = self.list_of_prices[:num_of_articles]
        return [SearchResultPage._parse_price(price) for price in article_to_parse]
