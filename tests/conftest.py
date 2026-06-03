from pathlib import Path
from random import randrange

import faker
import pytest

from logger import setup_logger
from pages.slider_page import SliderBoundaries

fake = faker.Faker()


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com"


@pytest.fixture
def basic_auth_url():
    return {
        "url": "https://the-internet.herokuapp.com/basic_auth",
        "username": "admin",
        "password": "admin",
    }


@pytest.fixture
def get_slider_value() -> tuple[int, str]:
    """Возвращает кол-во нажатия клавиши RightArrow и ожидаемое значение для аргумента .slider_value у экземпляра
    SliderPage"""
    value = randrange(SliderBoundaries.MIN, SliderBoundaries.MAX)
    return value, f"{value / 2:.1f}" if value % 2 != 0 else f"{value / 2:.0f}"


@pytest.fixture
def tmp_text_file():
    file_path = Path("tests/test_file.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fake.text())
    yield file_path
    file_path.unlink()


@pytest.fixture
def clear_filepath():
    file_path = Path("tests/downloaded_file/")
    for file in file_path.iterdir():
        file.unlink()
