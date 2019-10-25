from time import sleep
from YouShuYun_APP.base.base_driver import BaseDriver
from selenium.webdriver.common.by import By

class UserPage(BaseDriver):
    def click_login_avatar(self):
        # 点击头像登录入口
        self.driver.find_element(By.ID, "clickArea").click()
        return self

    def wechat_login(self):
        # 选择、点击，微信登录
        self.driver.find_element(By.ID, "tvWeixin").click()
        return self

    def qq_login(self):
        # 选择、点击，QQ登录
        self.driver.find_element(By.ID, "id/tvQQ").click()
        return self

    def phone_login(self, phone):
        # 输入手机号
        self.driver.find_element(By.ID, "inputPhone").send_keys(phone)
        return self

    def phone_code_login(self, code):
        # 输入手机验证码
        self.driver.find_element(By.ID, "inputCode").send_keys(code)
        return self

    def click_login_button(self):
        # 手机号方式，点击【登录】按钮
        self.driver.find_element(By.ID, "tvLogin").click()
        return self