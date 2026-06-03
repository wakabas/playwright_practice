from playwright.sync_api import Page

from pages.download_page import DownloadPage


def test_download(page: Page, base_url: str, clear_filepath):
    download_page = DownloadPage(page)
    download_page.action.goto(f"{base_url}/download")
    expected_file_name = download_page.get_filename_for_download()
    received_file_name = download_page.get_downloaded_filename()
    assert expected_file_name == received_file_name, (
        f"Expected filename {expected_file_name} but got {received_file_name}"
    )
