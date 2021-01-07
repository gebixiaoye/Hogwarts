import pytest
import yaml


class Test_demo():

    #参数化，第一个参数为入参一致，第二组为数据,ids为别名
    @pytest.mark.parametrize("a,b,result",
            yaml.safe_load(open("data.yml"))["datas"]
    ,ids=['int','minus','bigint'])
    def test_one(self,a,b,result):
        assert a+b == result
        print("这是我的测试用例")

    @pytest.mark.parametrize('a',[1,2])
    @pytest.mark.parametrize('b',[3,4])
    def test_two(self,a,b):
        print("测试数据组合使用：a->%s,b->%s"%(a,b))