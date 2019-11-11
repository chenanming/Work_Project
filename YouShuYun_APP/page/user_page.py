from time import sleep
from YouShuYun_APP.base.base_driver import BaseDriver
from selenium.webdriver.common.by import By

class UserPage(BaseDriver):
    def click_login_avatar(self):
        # 点击头像登录入口
        self.driver.find_element(By.ID, "clickArea").click()
        # self.driver.find_element(By.ID, self.readini.get_value('UserPage', '头像登录入口')).click()
        return self

    def wechat_login(self):
        # 选择、点击，微信登录
        self.driver.find_element(By.ID, "tvWeixin").click()
        # self.driver.find_element((By.ID, self.readini.get_value('UserPage', 'WeChat登录方式')))
        return self

    def qq_login(self):
        # 选择、点击，QQ登录
        self.driver.find_element(By.ID, "id/tvQQ").click()
        # self.driver.find_element(By.ID, self.readini.get_value('UserPage', 'QQ登录方式'))
        return self

    def phone_login(self, phone):
        # 输入手机号
        self.driver.find_element_by_id("com.youshuge.happybook:id/inputPhone").send_keys(phone)
        # self.driver.find_element(By.ID, self.readini.get_value('UserPage', '手机号输入框')).send_keys(phone)
        return self

    def phone_code_login(self, code):
        # 输入手机验证码
        self.driver.find_element_by_id("com.youshuge.happybook:id/inputCode").send_keys(code)
        # self.driver.find_element(By.ID, self.readini.get_value('UserPage', '验证码输入框')).send_keys(code)
        return self

    def click_login_button(self):
        # 手机号方式，点击【登录】按钮
        self.driver.find_element(By.ID, "tvLogin").click()
        # self.driver.find_element(By.ID, self.readini.get_value('UserPage', '登录按钮')).click()
        return self