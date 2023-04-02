import json
from pathlib import Path


SETTINGS_FILE = Path("settings.json")


class _SettingsConfig:
    def __init__(self):
        if not self.__checkSettingsConfigIsExists():
            self.__createSettingsConfig()
        self.__settings = self.__loadSettings()

    def __checkSettingsConfigIsExists(self):
        return True if SETTINGS_FILE.exists() else False

    def __createSettingsConfig(self):
        __settings = {
            "host": "None",
            "port": "None",
            "email": "None",
            "password": "None"
        }
        with SETTINGS_FILE.open("w", encoding="utf-8") as __settingsConfig:
            json.dump(__settings, __settingsConfig, ensure_ascii=False, indent=4)

    def __loadSettings(self):
        with SETTINGS_FILE.open(encoding="utf-8") as __settingsConfig:
            __settings = json.load(__settingsConfig)
            return __settings

    @property
    def settings(self):
        return self.__settings


settingsConfig = _SettingsConfig()