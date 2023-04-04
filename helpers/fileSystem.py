import os
import shutil
from pathlib import Path
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)


class _FileSystem:
    def __init__(self):
        pass

    def getFilename(self, path, suffix=False):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        return path.stem if suffix is False else path.name

    def isEmpty(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if not path.is_dir():
            raise IsNotDirectoryException(path)
        if not len(os.listdir(path)) == 0:
            raise IsNotEmptyException(path)
        return True

    def makeDir(self, path, recreate=False):
        path = Path(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if (path.exists() and recreate is False):
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True

    def remove(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    def removeDir(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if not self.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    def removeTree(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                self.removeTree(child)
        path.rmdir()
        return True

    def exists(self, path):
        return Path(path).exists()

    def copyFile(self, path, newPath):
        path = Path(path)
        newPath = Path(newPath)
        if not path.exists():
            raise PathNotFoundException(path)
        if newPath.exists():
            raise PathExistsException(newPath)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        shutil.copy(path, newPath)


fileSystem = _FileSystem()
