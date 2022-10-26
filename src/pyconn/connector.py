""" 연결 인터페이스 정의
"""

from abc import ABC, abstractmethod
from sqlite3 import connect


class Connector(ABC):
    """ 인터페이스 클래스 입니다.
    """

    @abstractmethod
    def __init__(self, **kwargs):
        connect(**kwargs)

    @abstractmethod
    def connect(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def close(self) -> bool:
        pass


class FileConnector(Connector):
    """ 파일 연결 인터페이스 클래스 입니다.
    """
    @abstractmethod
    def upload_file(self, local_path: str, remote_path: str) -> bool:
        pass

    @abstractmethod
    def download_file(self, remote_path: str, local_path: str) -> bool:
        pass

    @abstractmethod
    def upload_dir(self, local_path: str, remote_path: str) -> int:
        pass

    @abstractmethod
    def download_dir(self, remote_path: str, local_path: str) -> int:
        pass
