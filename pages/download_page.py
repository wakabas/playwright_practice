from enum import IntEnum, StrEnum
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class PathForDownload(StrEnum):
    PATH = "tests/downloaded_file/"


class FileIndex(IntEnum):
    INDEX = 2


class DownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.file_for_download = MultiWebElement(
            self.page.locator("//div[@id='content']//a"),
            description="Download page -> links to download file",
        )

    def get_downloaded_filename(self, index: int = FileIndex.INDEX) -> str:
        with self.action.expect_download() as download_info:
            self.file_for_download.nth(index).click()
        download = download_info.value
        file_path = Path(PathForDownload.PATH + download.suggested_filename)
        download.save_as(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        return file_path.name

    def get_filename_for_download(self, index: int = FileIndex.INDEX) -> str:
        return self.file_for_download.nth(index).get_inner_text()
