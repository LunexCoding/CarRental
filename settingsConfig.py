from decouple import config


class _SettingsConfig:
    def __init__(self):
        self.__settingsConfig = self.__loadSettings()

    def __loadSettings(self):
        __settings = {}
        __settings["FTP"] = dict(
            host=config("FTP_HOST"),
            port=config("FTP_PORT", cast=int),
            login=config("FTP_LOGIN"),
            password=config("FTP_PASSWORD"),
            timeout=config("FTP_TIMEOUT", default=20, cast=int)
        )
        __settings["DATABASE"] = dict(
            host=config("DB_HOST"),
            port=config("DB_PORT", cast=int),
            user=config("DB_USER"),
            password=config("DB_PASSWORD"),
            database=config("DB_NAME")
        )
        __settings["SMTP"] = dict(
            host=config("SMTP_HOST"),
            port=config("SMTP_PORT", cast=int),
            email=config("SMTP_EMAIL"),
            password=config("SMTP_PASSWORD")
        )
        __settings["ADMIN"] = dict(
            token=config("ADMIN_TOKEN")
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