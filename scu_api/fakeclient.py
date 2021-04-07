
from .client import *
from .utils import *
from .spider import Spider
from .cache_table import CacheTable
from .constant import ClientStatus


class FakeClient(SCUClient):
    '''
    定义一个登陆SCU教务处的假用户
    '''

    def __init__(self):
        self.spider = Spider()
        self.cache = CacheTable()
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

    def get_student_name(self, use_cache: bool) -> Tuple[bool, str]:
        if use_cache and self.cache.exist('student_name'):
            return True, self.cache.query('student_name')

        if not self.session_valid():
            return False, '会话已过期，请重新登陆'

        success, stdname = self.spider.fetch_student_name()
        if success:
            self.cache.update('student_name', stdname)
        return success, stdname

    def get_student_pic(self, use_cache: bool, filepath: str = None) -> Tuple[bool, str]:
        if use_cache and self.cache.exist('student_pic'):
            pic = self.cache.query('student_pic')
            if filepath:
                with open(filepath, 'wb') as imfile:
                    imfile.write(base64Img_decode(pic))
            return True, pic

        if not self.session_valid():
            return False, '会话已过期，请重新登陆'

        success, stdpic = self.spider.fetch_student_pic(filepath)
        if success:
            self.cache.update('student_pic', stdpic)

        return success, stdpic
