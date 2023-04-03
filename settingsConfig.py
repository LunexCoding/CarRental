import json
from pathlib import Path
from decouple import config



class _SettingsConfig:
    def __init__(self):
        self.__settingsConfig = self.__loadSettings()

    def __loadSettings(self):
        __settings = {}
        __settings["FTP"] = dict(
            host=config("FTP_HOST", default=""),
            port=int(config("FTP_PORT", default="")),
            login=config("FTP_LOGIN", default=""),
            password=config("FTP_PASSWORD", default=""),
            timeout=int(config("FTP_TIMEOUT", default=""))
        )
        __settings["DATABASE"] = dict(
            host=config("DB_HOST", default=""),
            port=int(config("DB_PORT", default="")),
            user=config("DB_USER", default=""),
            password=config("DB_PASSWORD", default=""),
            database="AutoService"
        )
        __settings["SMTP"] = dict(
            host=config("SMTP_HOST", default=""),
            port=int(config("SMTP_PORT", default="")),
            email=config("SMTP_EMAIL", default=""),
            password=config("SMTP_PASSWORD", default="")
        )
        __settings["ADMIN"] = dict(
            token=config("ADMIN_TOKEN", default="")
        )
        return __settings

    @property
    def FTPSettings(self):
        return self.__settingsConfig["FTP"]

    @property
    def DatabaseSettings(self):
        return self.__settingsConfig["DATABASE"]

    @property
    def SMTPSettings(self):
        return self.__settingsConfig["SMTP"]

    @property
    def AdminSettings(self):
        return self.__settingsConfig["ADMIN"]


settingsConfig = _SettingsConfig()