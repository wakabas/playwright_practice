import json


class ConfigReader:
    _instance = None
    _filename = None


    def __new__(cls, filename: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            if cls._filename is None:
                cls._instance.read_config(filename)
            else:
                return cls._instance
        return cls._instance

    @classmethod
    def read_config(cls, filename: str) -> None:
        with open(filename, mode="r", encoding="utf-8") as f:
            cls._filename = filename
            cls._instance.config = json.load(f)

