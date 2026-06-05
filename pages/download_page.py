from enum import StrEnum
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class DownloadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.file_for_download = MultiWebElement(
            self.page.locator("//*[@id='content']//a"),
            description="Download page -> links to download file",
        )

    def get_downloaded_filename(self, path_to_download: Path, index: int) -> str:
        with self.action.expect_download() as download_info:
            self.file_for_download.nth(index).click()
        download = download_info.value
        file_path = Path(f"{path_to_download}/{download.suggested_filename}")
        download.save_as(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        return file_path.name

    def get_filename_for_download(self, index: int) -> str:
        return self.file_for_download.nth(index).get_inner_text()
