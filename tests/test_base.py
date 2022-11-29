import sys
sys.path.append('../')
import scu_api

bot = scu_api.get_student(scu_api.StudentType.UNDERGRADUATE)

def test_captcha():
    resp = bot.get_captcha()
    assert resp.is_ok()