
from .client import *
from .utils import password_encryption
from .spider import Spider


class FakeClient(SCUClient):
    '''
    定义一个登陆SCU教务处的假用户
    '''

    def __init__(self):
        self.spider = Spider()
        self.student_name = None
        

    def set_baseinfo(self, stid: str, passwd: str, hashed: bool = False):
        self.student_id = stid
        self.passwd_hash = passwd
        if not hashed:
            self.passwd_hash = password_encryption(passwd)
        self.status = ClientStatus.OFFLINE # 更换信息后强制下线

    def get_captcha(self, filepath: str = None) -> Tuple[bool, str]:
        return self.spider.fetch_captcha(filepath)

    def login(self, captcha: str, remember_me: bool) -> Tuple[bool, ]:
        if self.status == ClientStatus.INIT:
            return False
        success, _ = self.spider.login(self.student_id, self.passwd_hash, captcha, remember_me)
        self.status = [ClientStatus.OFFLINE, ClientStatus.ONLINE][success]
        return success, _

    def session_valid(self) -> bool:
        if self.status == ClientStatus.ONLINE:
            return True  # for test
        return False

    def get_student_name(self, use_cache: bool) -> Tuple[bool, str]:
        if use_cache and self.student_name:
            return True, self.student_name

        if not self.session_valid():
            return False, '会话已过期，请重新登陆账号'

        success, stdname = self.spider.fetch_student_name()
        if success:
            self.student_name = stdname
        return success, stdname

    def get_student_pic(self, use_cache: bool, filepath: str = None) -> Tuple[bool, str]:

        return True, ''
