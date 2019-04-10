import hashlib
import requests
import random

API = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
APPID = '******'
SECRET = '******'
md5 = hashlib.md5()


def translate(s):
    salt = str(random.randint(10000, 99999))
    sign = (APPID + s + salt + SECRET).encode('utf-8')
    md5.update(sign)
    sign = md5.hexdigest()
    params = {
        'q': s,
        'from': 'en',
        'to': 'zh',
        'appid': APPID,
        'salt': salt,
        'sign': sign
    }
    resp = requests.post(API, data=params)
    result = resp.json()
    try:
        trans_result = result['trans_result'][0]['dst']
    except KeyError:
        print(result['error_code'], ':', result['error_msg'])
        return None

    return trans_result


if __name__ == '__main__':
    s = input()
    print(translate(s))
