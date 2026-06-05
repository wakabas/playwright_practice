import pytest
from playwright.sync_api import Page

from pages.frame_page import FrameNames, FramePage


@pytest.mark.parametrize(
    "frame_name",
    [
        FrameNames.LEFT_NAME,
        FrameNames.RIGHT_NAME,
        FrameNames.BOTTOM_NAME,
        FrameNames.MIDDLE_NAME,
    ],
)
def test_frame_page(page: Page, base_url: str, frame_name: FrameNames):
    frame_page = FramePage(page)
    frame_page.action.goto(f"{base_url}/nested_frames")
    received_text = frame_page.get_frame_text(frame_name)
    expected_text = FramePage.FRAME_MAP[frame_name]
    assert received_text == expected_text, (
        f"Expected text - {expected_text}, but got {received_text}"
    )
