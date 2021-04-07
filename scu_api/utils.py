# -*- coding: utf-8 -*-

import hashlib
import base64

def password_encryption(password: str) -> str:
    hlmd5 = hashlib.md5()
    hlmd5.update(password.encode('utf-8'))
    return hlmd5.hexdigest()

def base64Img_encode(image: bytes) -> str:
    return str(base64.b64encode(image), 'utf-8')
