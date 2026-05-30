import re
import logging
from enum import StrEnum

from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

class HtmlAttributes(StrEnum):
    AVATAR = "User Avatar"
    USERNAME = "name: user"


class HoverPage:
    def __init__(self, page: Page):
        self.page = page
        self.action = PageActions(page)
        self.user_avatars = MultiWebElement(
            self.page.get_by_alt_text(HtmlAttributes.AVATAR),
            "Hover page -> user avatars",
        )
        self.user_names = MultiWebElement(
            self.page.locator(
                "div.figcaption", has_text=re.compile(HtmlAttributes.USERNAME)
            ),
            description="Hover page -> user name",
        )

    @classmethod
    def _format_username_text(cls, username_text: str) -> str:
        result = username_text.split("\n")[0]
        logger.info(f"Hover page -> username formatted '{result}'")
        return result

    def _wait_for_visible_avatars(self):
        self.user_avatars.wait_for_first_element()


    def get_user_names(self) -> list[str]:
        result = []
        self._wait_for_visible_avatars()
        user_avatars, user_names = self.user_avatars.all(), self.user_names.all()
        for user_avatar, user_name in zip(user_avatars, user_names):
            user_avatar.hover()
            result.append(HoverPage._format_username_text(user_name.get_inner_text()))
        if not result:
            logger.error("Users not found on page")
            raise ValueError("No users found")
        return result
