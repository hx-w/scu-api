# -*- coding: utf-8 -*-

import functools
import requests

from .logger import get_mylogger

logger = get_mylogger('Request')

def req_logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                return func(*args, **kw)
            except Exception as ept:
                logger.error('%s %s()  [%s]' %(text, func.__name__, ept))
            return func(*args, **kw)
        return wrapper
    return decorator

class Spider:
    def __init__(self):
    
        ...
    
    @req_logger
    def fetch_captcha(self) -> str:
        pass