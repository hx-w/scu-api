# scu-api
Provide an api for Sichuan University


## Usage

```python
get_fakeclient()  # 获取FakeClient实例

```


[TODO]

## Example

```python
import scu_api

fakeclient = scu_api.get_fakeclient()

fakeclient.set_baseinfo(
    'student_id',
    'password',
    False
)

success, _ = fakeclient.get_captcha(filepath='captcha.jpg')

captcha = input('输入验证码:')

success, _ = fakeclient.login(captcha, True)

success, std_name = fakeclient.get_student_name(True)

print(std_name)
```