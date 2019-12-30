#!/usr/bin/python3
# -*- coding=utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from unit.read_element import ReadInit


class BaseDriver:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.readini = ReadInit()