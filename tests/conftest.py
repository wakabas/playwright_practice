from random import randrange

import pytest

from logger import setup_logger


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
    value = randrange(1, 9)
    return value, f"{value / 2:.1f}" if value % 2 != 0 else f"{value / 2:.0f}"
