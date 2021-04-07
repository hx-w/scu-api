# -*- coding: utf-8 -*-

class CacheTable:
    def __init__(self):
        self.table = {
            'student_name': None,
            'student_pic': None
        }
    
    def exist(self, key: str) -> bool:
        return key in self.table.keys() and self.table.get(key)
    
    def query(self, key: str):
        return self.table.get(key)

    def update(self, key: str, val):
        self.table[key] = val

    def clear(self):
        self.__init__()
    