import scu_api

fakeclient = scu_api.get_fakeclient()

fakeclient.set_baseinfo(
    '2017141461079',
    'Hexiang811021',
    False
)

print(fakeclient.get_captcha())