
from .client import *
from .utils import *
from .spider import Spider
from .constant import ClientStatus


class FakeClient(SCUClient):
    '''
    定义一个登陆SCU教务处的假用户
    '''

    def __init__(self):
        self.spider = Spider()
        self.student_id = None
        self.passwd_hash = None
        self.status = ClientStatus.INIT

    def set_baseinfo(self, stid: str, passwd: str, hashed: bool = False):
        self.student_id = stid
        self.passwd_hash = passwd
        if not hashed:
            self.passwd_hash = password_encryption(passwd)
        self.status = ClientStatus.OFFLINE  # 更换信息后强制下线

    def get_captcha(self, filepath: str = None) -> Tuple[bool, str]:
        return self.spider.fetch_captcha(filepath)

    def login(self, captcha: str, remember_me: bool) -> Tuple[bool, ]:
        if self.status == ClientStatus.INIT:
            return False
        success, _ = self.spider.login(
            self.student_id, self.passwd_hash, captcha, remember_me)
        self.status = [ClientStatus.OFFLINE, ClientStatus.ONLINE][success]
        return success, _

    def session_valid(self) -> bool:
        if self.status == ClientStatus.ONLINE:
            return True  # for test
        return False

    def get_student_name(self) -> Tuple[bool, str]:
        if not self.session_valid():
            return False, '会话已过期，请重新登陆'
        return self.spider.fetch_student_name()

    def get_student_pic(self, filepath: str = None) -> Tuple[bool, str]:
        if not self.session_valid():
            return False, '会话已过期，请重新登陆'
        return self.spider.fetch_student_pic(filepath)
