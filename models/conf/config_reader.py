import json


class ConfigReader:
    _instance = None
    _filename = None

    def __new__(cls, filename: str):
        if cls._filename is None:
            cls._instance = super().__new__(cls)
            cls.read_config(filename)
        if filename == cls._filename:
            return cls._instance
        else:
            cls._instance = super().__new__(cls)
            cls.read_config(filename)
        return cls._instance

    @classmethod
    def read_config(cls, filename: str) -> None:
        with open(filename, mode="r", encoding="utf-8") as f:
            cls._instance.config = json.load(f)
