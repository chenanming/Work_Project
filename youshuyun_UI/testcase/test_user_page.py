#!/usr/bin/python3
# -*- coding=utf-8 -*-
import pytest, allure
from YouShuYun_UI.testpage.home_page import HomePage

@allure.feature("测试-登录、退出流程")
class TestLogin:
    def setup(self):
        self.userpage = HomePage()

    def teardown(self):
        self.userpage.goto_user().click_set_button(5).click_logout_button()
        self.userpage.driver.quit()

    @allure.story("测试-微信登录方式")
    def test_wechat_login(self):
        ''' 测试01：微信登录
        '''
        self.userpage.goto_user().click_login_avatar().wechat_login()
        assert self.userpage.get_toast('登录成功') == True

    @allure.story("测试-QQ登录方式")
    def test_qq_login(self):
        ''' 测试02：QQ登录
        '''
        self.userpage.goto_user().click_login_avatar().qq_login()
        assert self.userpage.get_toast('登录成功') == True

    @allure.story("测试-手机号登录方式")
    def test_phone_login(self):
        ''' 测试03：手机号验证登录
        '''
        self.userpage.goto_user().click_login_avatar().phone_login('18888888888').phone_code_login('666666').click_login_button()
        assert self.userpage.get_toast('登录成功') == True