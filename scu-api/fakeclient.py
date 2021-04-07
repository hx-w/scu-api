
from .constant import ClientStatus
from .client import SCUClient
from .utils import password_encryption

class FakeClient(SCUClient):
    '''
    定义一个登陆SCU教务处的假用户
    '''
    def __init__(self):
        ...
    
    def set_baseinfo(self, stid: str, passwd: str, hashed: bool=False):
        self.student_id = stid
        self.passwd_hash = passwd
        if not hashed:
            self.passwd_hash = password_encryption(passwd)
        self.status = ClientStatus.OFFLINE


    def login(self, lt: bool) -> ClientStatus:

        pass
