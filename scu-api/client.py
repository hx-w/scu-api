# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

class SCUClient(metaclass=ABCMeta):
    def __init__(self):
        self.student_id = None
        self.passwd_hash = None
        self.student_name = None
        self.pic_url = None
    
    @abstractmethod
    def set_baseinfo(self):
        # set student_id & passwd_hash
        ...

    @abstractmethod
    def get_status(self):
        ...
    
    @abstractmethod
    def login(self, lt: bool) -> bool:
        # 
        ...
    
    @abstractmethod
    def get_student_name(self, use_cache:bool=True) -> tuple(bool, str):
        ...
    
    @abstractmethod
    def get_pic_url(self, use_cache:bool=True) -> tuple(bool, str):
        ...