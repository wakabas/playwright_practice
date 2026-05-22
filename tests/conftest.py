import pytest

from models.conf.config_reader import ConfigReader

CONFIG = ConfigReader()


@pytest.fixture
def url():
    url = CONFIG.config["URL"]
    return url


@pytest.fixture
def browser_name():
    browser_name = CONFIG.config["browser"]
    return browser_name
