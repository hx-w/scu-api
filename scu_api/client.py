# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from typing import Tuple

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
    def get_captcha(self, filepath: str=None) -> Tuple[bool, str]:
        '''
        @brief 获取验证码
        @param[in]  filepath(str)  [可选的] 存储验证码图像的全路径，使用**.jpg**格式
        @param[out] success(bool)  操作是否成功
        @param[out] str(bool)      验证码图像base64编码
        '''

    @abstractmethod
    def login(self, catpcha: str, remember_me: bool) ->  Tuple[bool,]:
        '''
        @brief 模拟登陆
        @param[in] captcha(str) 通过get_captcha获取的验证码识别后的字符串
        @param[in] remember_me(bool) 是否开启两周内快速登录
        @param[out] success(bool) 是否登录成功
        '''
        ...
    
    @abstractmethod
    def get_student_name(self, use_cache:bool=True) -> Tuple[bool, str]:
        ...
    
    @abstractmethod
    def get_pic_url(self, use_cache:bool=True) -> Tuple[bool, str]:
        ...
