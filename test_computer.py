from  computer import *
import pytest


class Test_computer():

    def setup_method(self):
        print("测试用例之前执行,开始计算")

    def teardown_method(self):
        print("\n每个测试用例之后执行,计算结束")

    @pytest.mark.parametrize('operator,a,b,result',[
        ('add',1,4,5),('sub',5,2,3),('mul',4,5,20),('div',30,6,5)
    ])
    def test_operator(self,operator,a,b,result):
        if operator == 'add':
            assert add(a,b) == result
        elif operator == 'sub':
            assert  sub(a,b) == result
        elif operator == 'mul':
            assert mul(a,b) == result
        elif operator == 'div' :
            assert div(a,b) == result
        else: print("无此运算符")


# if __name__ == '__main__':
#     test_computer()
#
