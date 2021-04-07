
from .client import *
from .utils import password_encryption
from .spider import Spider

class FakeClient(SCUClient):
    '''
    定义一个登陆SCU教务处的假用户
    '''
    def __init__(self):
        self.spider = Spider()
    
    def set_baseinfo(self, stid: str, passwd: str, hashed: bool=False):
        self.student_id = stid
        self.passwd_hash = passwd
        if not hashed:
            self.passwd_hash = password_encryption(passwd)
        self.status = ClientStatus.OFFLINE


    def get_captcha(self, filepath: str=None) -> Tuple[bool, str]:
        success, b64Image = self.spider.fetch_captcha()


    def login(self, captcha: str, remember_me: bool) -> Tuple[bool,]:
        if self.status == ClientStatus.INIT:
            return False
        return self.spider.login(self.student_id, self.passwd_hash, captcha, remember_me)


    def get_status(self) -> ClientStatus:
        return ClientStatus.INIT # FOR TEST

    def get_pic_url(self, use_cache: bool) -> Tuple[bool, str]:
        return True, ''
    
    def get_student_name(self, use_cache: bool) -> Tuple[bool, str]:
        return True, ''