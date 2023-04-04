from ftplib import FTP
from pathlib import Path
from settingsConfig import settingsConfig

FTP_SERVER_IMAGE_DIRECTORY = "image"
IMAGE_CARS = Path("imageCars")


class _FTPServer:

    statuses = ['unlocked', 'locked']

    def __init__(self, __settings):
        self.__settings = __settings
        self.__host = __settings["host"]
        self.__port = __settings["port"]
        self.__login = __settings["login"]
        self.__password = __settings["password"]
        self.__timeout = __settings["timeout"]
        self._ftp = FTP()

    def connectServer(self):
        self._ftp.connect(self.__host, self.__port, self.__timeout)
        self._ftp.login(self.__login, self.__password)
        self._ftp.set_pasv(True)
        return self._ftp

    def uploadFile(self, path):
        self.connectServer()
        self._ftp.cwd(FTP_SERVER_IMAGE_DIRECTORY)
        path = Path(path)
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                with path.open('rb') as file:
                    self._ftp.storbinary('STOR ' + path.name, file, 1024)
                    self.statusUnlocked()
            except Exception as e:
                self.statusUnlocked()
        self.closeConnect()

    def downloadFile(self, filename):
        self.connectServer()
        self._ftp.cwd(FTP_SERVER_IMAGE_DIRECTORY)
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                with Path(IMAGE_CARS / filename).open('wb') as file:
                    self._ftp.retrbinary('RETR ' + filename, file.write)
                    self.statusUnlocked()
            except Exception as e:
                self.statusUnlocked()

    def deleteFile(self, path):
        self.connectServer()
        self._ftp.cwd(FTP_SERVER_IMAGE_DIRECTORY)
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                self._ftp.delete(path)
                self.statusUnlocked()
            except:
                self.statusUnlocked()
        self.closeConnect()

    def statusUnlocked(self):
        self._ftp.rename('locked', 'unlocked')

    def statusLocked(self):
        self._ftp.rename('unlocked', 'locked')

    def getStatus(self):
        for status in self._ftp.nlst():
            if status in _FTPServer.statuses:
                return status

    def listDir(self):
        self.connectServer()
        self._ftp.cwd(FTP_SERVER_IMAGE_DIRECTORY)
        files = []
        try:
            files = self._ftp.nlst()[2:]
            self.closeConnect()
            del files[-1]
            return files
        except:
            self.closeConnect()
            return files

    def createLocker(self):
        self.connectServer()
        if 'unlocked' and 'locked' not in self._ftp.nlst():
            open('../unlocked', 'wb').close()
            self._ftp.cwd(FTP_SERVER_IMAGE_DIRECTORY)
            self._ftp.storbinary('STOR unlocked', open('../unlocked', 'rb'))
        self.closeConnect()

    def closeConnect(self):
        self._ftp.close()

    def __del__(self):
        self.closeConnect()


ftpServer = _FTPServer(settingsConfig.FTPSettings)
ftpServer.createLocker()
