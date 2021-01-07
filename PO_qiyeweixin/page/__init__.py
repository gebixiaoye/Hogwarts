from PO_qiyeweixin.page.index_page import index_page1


class shouye:
    def goto_login(self):
        """登录页面"""


        return Loginpage1()


    def goto_register(self):
        """
        注册页面
        :return:
        """

        pass


class Loginpage1:

    def Login(self):
        """
        登录
        :return:
        """
        return index_page1()
