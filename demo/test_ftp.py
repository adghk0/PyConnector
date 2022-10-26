""" FTP 인터페이스 테스트 프로그램
"""

import os, sys


src_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'src')
sys.path.append(src_path)

from pyconn import FTPConnector


if __name__ == '__main__':
    ftp = FTPConnector('127.0.0.1', 21, 'ftp_user', '#ftp', 'euc-kr')
    
    # ftp.upload_file('C:/Data/Test/send한글.txt', '/test/test/test/')
    # ftp.download_file('/test.txt', 'C:/Data/Test/dir/dir2/test.txt')
    # ftp.upload_dir('C:/Data/Test/dir', '/test', mkdir=False)
    a = ftp.download_dir('/test', 'C:\\Data\\Test')
    print(a)