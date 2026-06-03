from playwright.sync_api import Page

from ui.page_actions import PageActions


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.action = PageActions(self.page)
