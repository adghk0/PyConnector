""" 탐색 인터페이스 정의
"""

import os
from typing import Any

from .connector import Connector
from abc import ABCMeta, abstractmethod


class Explorer(Connector):
    """ 기본 구조 탐색 클래스 입니다.
    """

    @abstractmethod
    def current(self) -> Any:
        """ 현재 탐색중인 항목을 반환합니다.
        """
        pass

    @abstractmethod
    def explore(self, target: Any):
        """ 입력받은 항목을 탐색합니다.
        """
        pass


class FileExplorer(Explorer):
    """ 파일 구조 탐색 클래스 입니다.
    """
    @abstractmethod
    def listdir(self, remote_path: str) -> list:
        pass
    
    @abstractmethod
    def exists(self, remote_path: str) -> bool:
        pass
    
    @abstractmethod
    def mkdir(self, remote_path: str) -> bool:
        pass
    
    @abstractmethod
    def isdir(self, remote_path: str) -> bool:
        pass

    @abstractmethod
    def isfile(self, remote_path: str) -> bool:
        pass

    """
    TODO : 구현 대상 메소드
    os.path.getatime
    os.path.getctime
    os.path.getmtime
    os.path.getsize
    os.path.isabs
    os.path.islink
    os.path.ismount
    os.path.lexists
    """