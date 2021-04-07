# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

from .constant import ClientStatus

class SCUClient(metaclass=ABCMeta):
    def __init__(self):
        self.student_id = None
        self.passwd_hash = None
        self.student_name = None
        self.pic_url = None
        self.status = ClientStatus.INIT
    
    @abstractmethod
    def set_baseinfo(self, stid: str, passwd: str, hashed: bool=False):
        '''
        @stid(str)    学号
        @passwd(str)  密码
        @hashed(bool) 密码是否已经过md5加密 default=False
        '''
        ...

    @abstractmethod
    def get_status(self) -> ClientStatus:
        ...
    
    @abstractmethod
    def login(self, lt: bool) ->  ClientStatus:
        # 
        ...
    
    @abstractmethod
    def get_student_name(self, use_cache:bool=True) -> tuple(ClientStatus, str):
        ...
    
    @abstractmethod
    def get_pic_url(self, use_cache:bool=True) -> tuple(ClientStatus, str):
        ...
