import time
import os

from qiniu import Auth, put_file

AK = '******'
SK = '******'
BUCKET = 'aimaster'


class Qiniu:

    def __init__(self):
        self.client = Auth(AK, SK)
        self.__key = str(int(time.time())) + '.txt'
        self.__bucket = BUCKET
        self.__token = self.client.upload_token(self.__bucket, self.__key, 60)

    def upload(self, filepath):
        ret, info = put_file(self.__token, self.__key, filepath)
        assert info.status_code == 200
        os.remove('test.txt')


client = Qiniu()

client.upload('test.txt')
