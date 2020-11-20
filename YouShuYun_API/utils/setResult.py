#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Time: 2020/11/4 0004 11:16
"""
:yamlset: 读取/写入，yaml文件
:RegExp: 正则提取
;regular： 提取响应的值，赋值、添加全局变量，
:variable: 全局变量池
:setResult: 接口返回值的提取，实现接口参数的传递的返回函数
"""

from requests import Response
from YouShuYun_API.utils.logger import log
from YouShuYun_API.common.RegExp import regexps as reg
from YouShuYun_API.common.yamlset import yaml_set
from YouShuYun_API.common.variable import is_vars
from YouShuYun_API.utils.serializa import is_json_str, deserialization
from YouShuYun_API.config.config import CF
# reg = Regular()


def get_var_result(r: Response, number, case):
    """替换变量"""
    if case[CF.EXTRACT_VARIABLE]:
        for i in case[CF.EXTRACT_VARIABLE].split(','):
            result = reg(i, r.text)
            is_vars.set(i, result)
            log.info(f"提取变量{i}={result}")
            if not is_vars.get(i):
                yaml_set.write_results(number, CF.EXTRACT_VARIABLE, f"提变量{i}失败")
    yaml_set.write_results(number, CF.RESPONSE_TEXT,
                            f"ResponseCode：{r.status_code}\nResponseText：{r.text}")


def replace_param(case):
    """传入参数"""
    if case[CF.PARAMETER]:
        if is_json_str(case[CF.PARAMETER]):
            is_extract = reg.findall(case[CF.PARAMETER])
            if is_extract:
                return deserialization(reg.subs(is_extract, case[CF.PARAMETER]))
    return deserialization(case[CF.PARAMETER])

if __name__ == "__main__":
	pass