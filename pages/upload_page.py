from enum import StrEnum
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class SuccessMessage(StrEnum):
    UPLOADED = "File Uploaded!"


class UploadPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.choose_file_btn = WebElement(
            self.page.locator("//input[@id='file-upload']"),
            description="Upload page -> choose file button",
        )
        self.upload_btn = WebElement(
            self.page.locator("//input[@id='file-submit']"),
            description="Upload page -> upload button",
        )
        self.success_msg = WebElement(
            self.page.get_by_text(SuccessMessage.UPLOADED),
            description="Upload page -> success upload message",
        )
        self.uploaded_file = WebElement(
            self.page.locator("//*[@id='uploaded-files']"),
            description="Upload page -> list of uploaded files",
        )

    def upload_file(self, file_path: Path):
        self.choose_file_btn.set_input_files(file_path)
        self.upload_btn.click()
