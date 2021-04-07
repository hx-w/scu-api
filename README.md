# scu-api
Provide an api for Sichuan University


## Usage

获取假用户`FakeClient`实例:

```python
import scu_api

my_client = scu_api.get_fakeclient()

```

`FakeClient`内置方法(目前为止)：
```python

@abstractmethod
def set_baseinfo(self, stid: str, passwd: str, hashed: bool = False):
    '''
    @stid(str)    学号
    @passwd(str)  密码
    @hashed(bool) 密码是否已经过md5加密 default=False
    '''

@abstractmethod
def session_valid(self) -> bool:
    '''
    @brief 返回网站会话是否有效，在有效的情况下才可以获取个人信息
            如果session过期，则需要获取验证码重新登陆
    @param[out] valid(bool)  网站会话是否有效
    '''

@abstractmethod
def get_captcha(self, filepath: str = None) -> Tuple[bool, str]:
    '''
    @brief 获取验证码
    @param[in]  filepath(str)  [可选的] 存储验证码图像的全路径，使用**.jpg**格式
    @param[out] success(bool)  操作是否成功
    @param[out] str(bool)      验证码图像base64编码
    '''

@abstractmethod
def login(self, catpcha: str, remember_me: bool) -> Tuple[bool, ]:
    '''
    @brief 模拟登陆
    @param[in] captcha(str) 通过get_captcha获取的验证码识别后的字符串
    @param[in] remember_me(bool) 是否开启两周内快速登录
    @param[out] success(bool) 是否登录成功
    '''

@abstractmethod
def get_student_name(self) -> Tuple[bool, str]:
    '''
    @brief 获取学生姓名
    @param[out] success(bool) 是否获取成功
    @param[out] student_name(str) 学生姓名/失败反馈内容
    '''

@abstractmethod
def get_student_pic(self, filepath: str = None) -> Tuple[bool, str]:
    '''
    @brief 获取学生照片
    @param[out] success(bool) 是否获取成功
    @param[out] student_pic(str) 图片的base64编码
    '''

```

## Example

```python
import scu_api

fakeclient = scu_api.get_fakeclient()

fakeclient.set_baseinfo(
    'student_id',
    'password',
    False # set True when password already encrypted by md5
)

# save current captcha image in `captcha.jpg`
success, _ = fakeclient.get_captcha(filepath='captcha.jpg')

# you can only handle captcha manually for now
captcha_str = input('please type captcha string: ')

# login scu with `remember_me on`
success, _ = fakeclient.login(captcha_str, True)

# get student name.
success, std_name = fakeclient.get_student_name()

print('Student:', std_name)

# save student picture in `student.jpg` which is shown in scu official
success, std_pic = fakeclient.get_student_pic('student.jpg')

```