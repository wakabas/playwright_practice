from pathlib import Path

from playwright.sync_api import Page

from pages.upload_page import SuccessMessage, UploadPage


def test_upload_page(page: Page, base_url: str, tmp_text_file: Path):
    upload_page = UploadPage(page)
    upload_page.action.goto(f"{base_url}/upload")
    upload_page.upload_file(tmp_text_file)
    received_msg = upload_page.success_msg.get_inner_text()
    assert received_msg == SuccessMessage.UPLOADED, (
        f"Expected text {SuccessMessage.UPLOADED}, but got {received_msg}"
    )
    received_filename = upload_page.uploaded_file.get_inner_text()
    assert tmp_text_file.name == received_filename, (
        f"Expected filename {tmp_text_file.name}, but got {received_filename}"
    )
