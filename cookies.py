from time import sleep

import yaml
from selenium import webdriver

import  unittest

class testwebdriver(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        with open("cookies_date.yaml",encoding="UTF-8") as f:
            self.cookies = yaml.safe_load(f)


        #获取cookies
        # self.cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #   'value': '1688853141845399'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #   'value': 'C04yhprDu9Sn0IoDmr7CGlbVjOMLMhrb5hwiu0B1y0zJejUc1d1wWPljXdpbWwbp3g_AyXd7Vr7HsNLlYLhoZTmLUdaqNSt2A2EiHmO0KNNgMIZzhVvnAN3UUSVg96sQqSEr4jyeKiMRSuwkZFAC_oXflLObSfjDHjT-EQvNrTxkckRgzI9qow4iz3MupSu2noJe7E4L83ZMb-mt5RmEh7hhO1Z4ZhymhpewL8powTsWuGGB3RnzrOVjF8BUUcWfCzNT6I1h2nJUPUuAyjuX_g'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #   'value': '1688853141845399'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #   'value': '1970325125207500'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #   'value': 'a7881694'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #   'value': '5HFc0uQkZm1GmjmuMHlTTEar_K0B9UVHbiHHlgCUbRBTx4GZ8L9VZSQuED-96Cij'},
        #  {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
        #   'value': 'ssid=s6504754125'},
        #  {'domain': 'work.weixin.qq.com', 'expiry': 1608417351, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #   'secure': False, 'value': '7qh7kot'},
        #  {'domain': '.qq.com', 'expiry': 1608472897, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #   'value': 'GA1.2.506228567.1608385819'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #   'path': '/', 'secure': False, 'value': '1608385873'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #   'value': '3756808305301582'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #   'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639921872, 'httpOnly': False,
        #                   'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                   'value': '1608385817'},
        #  {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #   'secure': False, 'value': '4150088354'},
        #  {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #   'value': 'direct'},
        #  {'domain': '.qq.com', 'expiry': 1671458497, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #   'value': 'GA1.2.695121634.1608385819'},
        #  {'domain': '.work.weixin.qq.com', 'expiry': 1639921815, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
        #   'secure': False, 'value': '0'},
        #  {'domain': '.work.weixin.qq.com', 'expiry': 1610978546, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #   'path': '/', 'secure': False, 'value': 'zh'}]




    def tearDown(self) -> None:
        # self.driver.quit()
        print('案例已结束')

    def test_get(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_link_text("企业登录").click()
        for cookie in self.cookies:
            self.driver.add_cookie(cookie)
        sleep(2)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id('menu_contacts').click()

        # print(self.driver.get_cookie())
        sleep(5)


class tesetWework(unittest.TestCase):
    def test_demo(self):
        """复用游览器，打印cookices
         命令窗口：Chrome - -remote-debugging-port=9222
        """
        opt = webdriver.ChromeOptions()

        opt.debugger_address = '127.0.0.1:9222'
        driver =webdriver.Chrome(options=opt)
        driver.get('https://work.weixin.qq.com/')

        sleep(8)

        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookie = driver.get_cookies()
        print(cookie)#打印cookies
        with open("cookies_date.yaml","w",encoding="UTF-8") as f:
            yaml.dump(cookie,f) #序列化 存储



# if __name__=='__main__':
#     tesetWework().test_demo()
    # unittest.main()