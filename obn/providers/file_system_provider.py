from abc import ABCMeta, abstractclassmethod
import os


class AbstractFileSystemProvider(metaclass=ABCMeta):
    """
    ファイルシステムを提供する抽象クラス
    """

    @abstractclassmethod
    def exist_directory(self, path: str) -> bool:
        """
        ディレクトリが存在するかを判定する
        """
        pass

    @abstractclassmethod
    def exist_file(self, path: str) -> bool:
        """
        ファイルが存在するかを判定する
        """
        pass


class FileSystemProvider(AbstractFileSystemProvider):
    """
    ファイルシステムを提供する実装クラス
    """

    def __init__(self):
        return

    def exist_directory(self, path):
        is_exist = os.path.exists(path)
        return is_exist

    def exist_file(self, path):
        is_exist = os.path.exists(path)
        return is_exist


class FileSystemProviderMock(AbstractFileSystemProvider):
    """
    ファイルシステムを提供するmockクラス
    """

    def __init__(self):
        return

    def exist_directory(self, dir_path):
        return True

    def exist_file(self, path):
        return True
