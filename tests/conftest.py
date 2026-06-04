from pathlib import Path
import tempfile
import os

import faker
import pytest

from logger import setup_logger
from conf.config_reader import ConfigReader

fake = faker.Faker()

@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="session")
def base_url():
    return "https://the-internet.herokuapp.com"

@pytest.fixture
def endpoint():
    return ConfigReader("conf/endpoints.json")


@pytest.fixture
def basic_auth_url():
    return {
        "url": "https://the-internet.herokuapp.com/basic_auth",
        "username": "admin",
        "password": "admin",
    }


@pytest.fixture
def tmp_text_file():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt", encoding="utf-8") as tmp:
        tmp.write(fake.text())
    yield tmp.name
    os.remove(tmp.name)


@pytest.fixture
def clear_filepath():
    file_path = Path("tests/downloaded_file/")
    for file in file_path.iterdir():
        file.unlink()
