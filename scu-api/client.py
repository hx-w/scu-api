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
    def get_captcha(self) -> tuple(bool, str):
        '''
        @brief 先获取验证码，再登陆
        @param[out] success(bool)  操作是否成功
        @param[out] str(bool)      验证码url
        '''

    @abstractmethod
    def login(self, lt: bool) ->  tuple(ClientStatus, str):
        # 尝试登录并获取验证码
        ...
    
    @abstractmethod
    def get_student_name(self, use_cache:bool=True) -> tuple(ClientStatus, str):
        ...
    
    @abstractmethod
    def get_pic_url(self, use_cache:bool=True) -> tuple(ClientStatus, str):
        ...
