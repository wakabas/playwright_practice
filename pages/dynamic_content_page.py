from enum import IntEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class NumOfOriginalAvatar(IntEnum):
    MIN = 2


class DynamicContentPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.user_avatars = MultiWebElement(
            self.page.locator("//*[contains(@class, 'large-2 columns')]/child::img"),
            description="Dynamic content page -> user avatars",
        )

    def get_unique_avatars_count(self):
        user_avatars = self.user_avatars.all()
        avatars_hrefs = {
            user_avatar.get_attribute("src") for user_avatar in user_avatars
        }
        return len(avatars_hrefs)

    def wait_for_unique_avatars(self):
        while True:
            num_of_unique_avatars = self.get_unique_avatars_count()
            if num_of_unique_avatars <= NumOfOriginalAvatar.MIN:
                return num_of_unique_avatars
            self.action.reload_page()
