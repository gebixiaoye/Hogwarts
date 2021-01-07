

class addressbook1:
    """通讯录页面"""

    def goto_addmenbers(self):
        '''添加成员'''
        from PO_qiyeweixin.page.addmenbers import addmenbers1

        return addmenbers1()

    def get_menbers(self):
        '''获取成员列表'''
        pass


    def goto_add_department(self):
        """添加部门
            弹窗创建部门名字

        """
        from PO_qiyeweixin.page.department import department1

        return department1()


    def goto_import_addressbook(self):
        """点击进入,导入通讯录"""
        pass


    def get_department(self):
        """
        获取部门列表
        :return:
        """
        departlis=[]
        return  departlis