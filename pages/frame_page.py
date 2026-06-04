from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class FrameNames(StrEnum):
    TOP_NAME = "frame-top"
    LEFT_NAME = "frame-left"
    MIDDLE_NAME = "frame-middle"
    RIGHT_NAME = "frame-right"
    BOTTOM_NAME = "frame-bottom"


class FrameText(StrEnum):
    LEFT_TEXT = "LEFT"
    MIDDLE_TEXT = "MIDDLE"
    RIGHT_TEXT = "RIGHT"
    BOTTOM_TEXT = "BOTTOM"


class FramePage(BasePage):
    FRAME_MAP = {
        FrameNames.LEFT_NAME: FrameText.LEFT_TEXT,
        FrameNames.MIDDLE_NAME: FrameText.MIDDLE_TEXT,
        FrameNames.RIGHT_NAME: FrameText.RIGHT_TEXT,
        FrameNames.BOTTOM_NAME: FrameText.BOTTOM_TEXT,
    }

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        top_frame = self.page.frame_locator(f"frame[name='{FrameNames.TOP_NAME}']")

        self.frame_left = WebElement(
            top_frame.frame_locator(f"frame[name='{FrameNames.LEFT_NAME}']")
            .locator("body"),
            description="Frame page -> left frame"
        )
        self.frame_middle = WebElement(
            top_frame.frame_locator(f"frame[name='{FrameNames.MIDDLE_NAME}']")
            .locator("body"),
            description="Frame page -> middle frame"
        )
        self.frame_right = WebElement(
            top_frame.frame_locator(f"frame[name='{FrameNames.RIGHT_NAME}']")
            .locator("body"),
            description="Frame page -> right frame"
        )
        self.frame_bottom = WebElement(
            self.page.frame_locator(f"frame[name='{FrameNames.BOTTOM_NAME}']")
            .locator("body"),
            description="Frame page -> bottom frame"
        )

    def get_frame_text(self, frame_name: StrEnum) -> str:
        frame_attr = "_".join(frame_name.split('-'))
        return self.__getattribute__(frame_attr).get_inner_text()


    @property
    def frames(self):
        return {
            FrameNames.LEFT_NAME: WebElement(
                self.page.frame(name=FrameNames.LEFT_NAME).locator("body"),
                description="Frame page -> left frame",
            ),
            FrameNames.MIDDLE_NAME: WebElement(
                self.page.frame(name=FrameNames.MIDDLE_NAME).locator("body"),
                description="Frame page -> middle frame",
            ),
            FrameNames.RIGHT_NAME: WebElement(
                self.page.frame(name=FrameNames.RIGHT_NAME).locator("body"),
                description="Frame page -> right frame",
            ),
            FrameNames.BOTTOM_NAME: WebElement(
                self.page.frame(name=FrameNames.BOTTOM_NAME).locator("body"),
                description="Frame page -> bottom frame",
            ),
        }
