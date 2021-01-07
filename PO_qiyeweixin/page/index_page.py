from PO_qiyeweixin.page.addmenbers import addmenbers1
from PO_qiyeweixin.page.addressbook import addressbook1
from PO_qiyeweixin.page.importAddressBook import importAddressBook1


class index_page1:
    '''企业微信主页'''

    def goto_addressbook(self):
        '''通讯录'''

        return addressbook1()

    def goto_addmenbers(self):
        '''添加成员'''

        return addmenbers1()

    def goto_import_addressbook(self):
        """导入通讯录"""

        return  importAddressBook1()