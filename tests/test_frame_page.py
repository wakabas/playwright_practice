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
    frame_map = frame_page.frames
    actual_text = frame_map[frame_name].get_inner_text()
    assert actual_text == FramePage.FRAME_MAP[frame_name], (
        f"Expected text - {FramePage.FRAME_MAP[frame_name]}, but got {actual_text}"
    )
