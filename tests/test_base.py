import sys
sys.path.append('../scu-api')
import scu_api

bot = scu_api.get_student(scu_api.Student_Type.UNDERGRADUATE)

def test_captcha():
    resp = bot.get_captcha()
    assert resp.is_ok()