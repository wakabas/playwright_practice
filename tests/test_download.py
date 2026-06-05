from pathlib import Path

from playwright.sync_api import Page

from pages.download_page import DownloadPage

path = Path("tests\downloaded_file\\")

def test_download(page: Page, base_url: str, endpoint, clear_filepath):
    download_page = DownloadPage(page)
    download_page.action.goto(f"{base_url}{endpoint[download_page.__class__.__name__]}")
    expected_file_name = download_page.get_filename_for_download(index=2)
    received_file_name = download_page.get_downloaded_filename(path, index=2)
    assert expected_file_name == received_file_name, (
        f"Expected filename {expected_file_name} but got {received_file_name}"
    )
