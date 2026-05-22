from models.pages.search_result_page import SearchResultPage


class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_bar = page.get_by_test_id("search-input")
        self.search_button = page.get_by_test_id("search-button")

    def search_articles(self, name: str):
        self.search_bar.fill(name)
        self.search_button.click()
        search_result_page = SearchResultPage(self.page)
        search_result_page.wait_for_load()
        return search_result_page
