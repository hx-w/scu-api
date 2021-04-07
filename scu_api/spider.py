# -*- coding: utf-8 -*-

import functools
import requests
import ujson
import re

from .logger import get_mylogger
from .utils import base64Img_encode

logger = get_mylogger('Request')

def req_logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                return True, func(*args, **kw)
            except Exception as ept:
                logger.error('%s [%s]' %(text, ept))
            return False, func(*args, **kw)
        return wrapper
    return decorator

class Spider:
    def __init__(self):
        self.session = requests.session()
        self.urls = {
            'captcha': 'http://zhjw.scu.edu.cn/img/captcha.jpg',
            'login': 'http://zhjw.scu.edu.cn/j_spring_security_check'
        }
    
        ...
    
    @req_logger('try fetch captcha')
    def fetch_captcha(self, filepath: str=None) -> str:
        captcha_resp = self.session.get(self.urls['captcha'])
        assert captcha_resp.status_code == requests.codes.ok, 'Network Issue'
        if filepath:
            with open(filepath, 'wb') as imfile:
                imfile.write(captcha_resp.content)
        return base64Img_encode(captcha_resp.content)
    
    @req_logger('try login')
    def login(self, stid: str, passwd: str, captcha: str, remb_me: bool) -> None:
        post_data = {
            'j_username': stid,
            'j_password': passwd,
            'j_captcha': captcha,
        }
        if remb_me:
            post_data['_spring_security_remember_me'] = 'on'
        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://zhjw.scu.edu.cn/login',
            'X-Requested-With': '',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Host': 'zhjw.scu.edu.cn',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36',
            'Origin':'http://zhjw.scu.edu.cn',
        }

        login_resp = self.session.post(url=self.urls['login'], data=post_data, headers=headers)
        assert login_resp.status_code == requests.codes.ok, 'Network Issue'

        assert not re.findall(r'errorCode=', login_resp.content.decode('utf-8'))