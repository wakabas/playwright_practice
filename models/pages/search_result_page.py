from enum import StrEnum


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
    def _parse_price(price: str):
        return int(price.split(maxsplit=1)[0])

    def get_article_prices(self, num_of_articles: int):
        result = [
            locator.inner_text()
            for locator in self.list_of_prices
        ]
        return [SearchResultPage._parse_price(price) for price in result][:num_of_articles]
