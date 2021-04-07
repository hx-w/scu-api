# scu-api
Provide an api for Sichuan University


## Usage

[TODO]

## Example

```python
import scu_api

fakeclient = scu_api.get_fakeclient()

fakeclient.set_baseinfo(
    'student id',
    'password',
    False
)

success, _ = fakeclient.get_captcha(filepath='captcha.jpg')

print('get_captcha', success)

captcha = input('输入验证码:')

success, _ = fakeclient.login(captcha, True)

print('login', success)

success, std_name = fakeclient.get_student_name(True)

print(success, std_name)

```