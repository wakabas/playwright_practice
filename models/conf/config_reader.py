import json


class ConfigReader:
    _instance = None
    FILENAME = "models/conf/config.json"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.read_config()
        return cls._instance

    @classmethod
    def read_config(cls):
        with open(ConfigReader.FILENAME, mode="r", encoding="utf-8") as f:
            cls._instance.config = json.load(f)
