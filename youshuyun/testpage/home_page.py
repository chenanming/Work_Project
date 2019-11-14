#!/usr/bin/python3
# -*- coding=utf-8 -*-
import logging
import pytest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from youshuyun.testpage.user_page import UserPage
from selenium.webdriver.common.by import By
from youshuyun.testunit.read_element import ReadInit

class HomePage:
    def __init__(self):
        capabilities = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:62027",
            "appPackage": "com.youshuge.happybook",
            "appActivity": "com.youshuge.happybook.ui.SplashActivity",
            "automationName": "Uiautomator2",
            "autoGrantPermissions": True,
            "noReset": "true",
            "unicodeKeyboard": True,  # 使用unicode编码方式发送字符串
            "resetKeyboard": True  # 绕过软键盘
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(15)


    def goto_book_details(self):
        pass

    def goto_bookcase(self):
        pass

    def goto_user(self):
        ''' 点击我的，“我的”页面
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # self.driver.find_element_by_android_uiautomator(self.value.get_value('UserPage', '我的')).click()
        return UserPage(self.driver)

    def get_toast(self, message):
        ''' 验证弹窗提示
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
            WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def get_attribute(self):
        #print(self.driver.find_element_by_id("clickArea").get_attribute("class"))
        print(self.driver.find_element_by_id("com.youshuge.happybook:id/inputPhone").get_attribute("class"))


    def get_page_source(self):
        ''' 获取页面信息
        '''
        try:
            text = self.driver.page_source
            logging.info("get page source success")
            return text
        except:
            logging.info("get page source is 'fail'")

    def swipeLeft(self, t=500, n=1):
        ''' 向左滑动屏幕
        '''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, t=500, n=1):
        ''' 向右滑动屏幕
        '''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipeDown(self, t=500, n=1):
        ''' 向下滑动屏幕
        '''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.35
        y2 = l['height'] * 0.65
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUp(self, t=500, n=1):
        ''' 向上滑动屏幕
        '''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.65
        y2 = l['height'] * 0.35
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

if __name__ == '__main__':
    pytest.main()