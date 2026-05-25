import json


class ConfigReader:
    _instance_map: dict = {}

    def __new__(cls, filename: str):
        if filename not in cls._instance_map:
            cls._read_config(filename)
        return cls._instance_map[filename]

    @classmethod
    def _read_config(cls, filename: str) -> None:
        with open(filename, mode="r", encoding="utf-8") as f:
            cls._instance_map[filename] = json.load(f)
