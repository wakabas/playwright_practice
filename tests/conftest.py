import pytest

from models.conf.config_reader import ConfigReader

CONFIG = ConfigReader("models/conf/config.json")


@pytest.fixture
def url():
    url = CONFIG["URL"]
    return url


@pytest.fixture
def browser_name():
    browser_name = CONFIG["browser"]
    return browser_name
