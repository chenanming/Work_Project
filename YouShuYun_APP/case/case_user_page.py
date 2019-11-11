#!/usr/bin/python3
# -*- coding=utf-8 -*-
from YouShuYun_APP.page.home_page import HomePage

class TestBookcase:
    def setup(self):
        self.userpage = HomePage()

    def teardown(self):
        self.userpage.driver.quit()

    def test_wechat_login(self):
        ''' 测试微信登录方式
        '''
        self.userpage.goto_user().click_login_avatar().wechat_login()
        assert self.userpage.get_toast('登录成功') == True

    def test_qq_login(self):
        ''' 测试QQ登录方式
        '''
        self.userpage.goto_user().click_login_avatar().qq_login()
        assert self.userpage.get_toast('登录成功') == True

    def test_phone_login(self):
        ''' 测试使用手机号验证登录方式
        '''
        self.userpage.goto_user().click_login_avatar().phone_login('18888888888').phone_code_login('666666').click_login_button()
        assert self.userpage.get_toast('登录成功') == True