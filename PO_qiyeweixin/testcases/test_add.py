from PO_qiyeweixin.page import shouye
from PO_qiyeweixin.page.index_page import index_page1


class Test_case():

    def setup(self):
        self.main = shouye()

    def test_cas1(self):
        """
        测试添加部门
        """
        # a =   self.main.goto_addressbook().goto_add_department().add_menbers().get_menbers()
        # assert  "测试部门" in a

        res =  self.main.goto_login().Login().goto_addressbook()
        assert "xx" in res