from enum import StrEnum

from playwright.sync_api import Locator


class Options(StrEnum):
    ASC = "price_asc"
    DESC = "price_desc"


class SearchResultPage:
    def __init__(self, page, num_of_articles: int | None = None):
        self.page = page
        self.results_loader = page.get_by_test_id("results-loader-svg")
        self.sort_list = page.get_by_test_id("filter-sort")
        self.apply_button = page.get_by_test_id("apply-filters-button")
        if num_of_articles is not None:
            self.list_of_prices = self.page.locator(
                "[data-testid^='search-result-price-']"
            ).all()[:num_of_articles]

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

    def get_article_prices(self) -> list[int]:
        return [SearchResultPage._parse_price(price) for price in self.list_of_prices]
