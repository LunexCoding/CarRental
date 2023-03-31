from ftplib import FTP
from decouple import config
from pathlib import Path
from helpers.fileSystem import fileSystem

FTP_SERVER_IMAGE_DIRECTORY = Path("image")
IMAGE_CARS = Path("imageCars")


class _FTPServer:

    statuses = ['unlocked', 'locked']

    def __init__(self, host=None, port=None, timeout=20):
        self._host = host
        self._port = port
        self._timeout = timeout
        self._ftp = FTP()

    def connectServer(self, username, password):
        self._ftp.connect(self._host, self._port, timeout=self._timeout)
        self._ftp.login(username, password)
        self._ftp.set_pasv(True)
        return self._ftp

    def uploadFile(self, path):
        path = Path(path)
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                with path.open('rb') as file:
                    self._ftp.storbinary('STOR ' + path.name, file, 1024)
                    self.statusUnlocked()
            except:
                self.statusUnlocked()

    def downloadFile(self, filename):
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                with Path(IMAGE_CARS / filename).open('wb') as file:
                    self._ftp.retrbinary('RETR ' + filename, file.write)
                    self.statusUnlocked()
            except:
                self.statusUnlocked()

    def deleteFile(self, path):
        if self.getStatus() == 'unlocked':
            self.statusLocked()
            try:
                self._ftp.delete(path)
                self.statusUnlocked()
            except:
                self.statusUnlocked()

    def statusUnlocked(self):
        self._ftp.rename('locked', 'unlocked')

    def statusLocked(self):
        self._ftp.rename('unlocked', 'locked')

    def getStatus(self):
        for status in self._ftp.nlst():
            if status in _FTPServer.statuses:
                return status

    def listDir(self):
        files = self._ftp.nlst()[2:]
        del files[-1]
        return files

    def createLocker(self):
        if 'unlocked' and 'locked' not in self._ftp.nlst():
            try:
                open('../unlocked', 'wb').close()
                self._ftp.cwd("image")
                self._ftp.storbinary('STOR unlocked', open('../unlocked', 'rb'))
            except Exception as e:
                print(e)

    def closeConnect(self):
        self._ftp.close()

    def __del__(self):
        self.closeConnect()


host = config("HOST", default="")
port = int(config("PORT", default=""))
login = config("LOGIN", default="")
password = config("PASSWORD", default="")

ftpServer = _FTPServer(host, port)
ftpServer.connectServer(login, password)
ftpServer.createLocker()



