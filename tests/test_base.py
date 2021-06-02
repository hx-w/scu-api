import sys
sys.path.append('..')
import scu_api

bot = scu_api.get_student(scu_api.Student_Type.UNDERGRADUATE)

def test_warning():
    resp = bot.get_student_name()
    assert not resp.is_ok()