# -*- coding: utf-8 -*-

from enum import Enum, auto
from typing import Any, Union
from collections import UserDict

#  Start-> INIT -> OFFLINE -> ONLINE
#                    |    <-     |

class Client_Status(Enum):
    INIT = auto()      # init state
    OFFLINE = auto()   # set baseinfo and without login
    # after login, MAYBE cache outdate in SCU website, need get_status() to check
    ONLINE = auto()

class API_Status(Enum):
    OK = 'ok'
    ERROR = 'error'
    WARNING = 'warning'
    UNKNOWN = 'unknown'

class API_ReturnType(UserDict):
    def __init__(self, status: API_Status, result: Any):
        self.data = {
            'status': status,
            'result': result
        }
    
    def is_ok(self) -> bool:
        return self.data['status'] == API_Status.OK

    def __missing__(self, _key: str):
        if isinstance(_key, str):
            raise KeyError(_key)
        return self[_key]
    
    def __getattr__(self, _key: str) -> Union[API_Status, Any]:
        return self.data[_key]
