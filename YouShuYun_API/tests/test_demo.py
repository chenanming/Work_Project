#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/4 0004 11:12
# @File: test_demo.py
# @Poject: Work_Project

import re

def get_failure_array(pattern):  # 制作部分匹配表
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i-1]
            continue
        j += 1
        failure.append(i)
    return failure


def kmp(pattern, text):
    failure = get_failure_array(pattern)  # 得到部分匹配表
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            if j == (len(pattern) - 1):
                return True
            j += 1
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return False


if __name__ == "__main__":
    print(kmp('123456', '123123456'))