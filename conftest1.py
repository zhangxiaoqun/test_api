# -*- coding: utf-8 -*-
# @File : conftest1.py
# @Software: PyCharm


from CRM_interface.Work_report import WorkReport as Wt
import pytest, time
from Crm_login.Login import get_token
from data.report_data import listData, add_report
from configs.config import CRM_PAW    # CRM_PAW:大数据账号



#本地时间
localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#登录
token = get_token(CRM_PAW)  # CRM_PAW:大数据账号


@pytest.fixture(scope='module', autouse=True)  # 环境初始化 、数据清除
def delete_all_(request):
    # 日报
    dailyList = Wt().list_Daily(token, listData[0], resText=True)["data"]["list"]
    # 周报
    weeklyList = Wt().list_weekly(token, listData[0], resText=True)["data"]["list"]
    # 月报
    MonthlyList = Wt().list_Monthly_report(token, listData[0], resText=True)["data"]["list"]
    # 专项汇报
    specialList = Wt().list_special(token, listData[0], resText=True)["data"]["list"]
    # 日报
    for Daily in dailyList:
        DailyId = Daily['id']  # 获取id
        # 删除所有的数据
        Wt().delete_Daily(token, DailyId)  # 删除日报
    # 周报
    for weekly in weeklyList:
        weeklyId = weekly['id']  # 获取id
        # 删除所有的数据
        Wt().delete_weekly(token, weeklyId)  # 删除周报
    # 月报
    for Monthly in MonthlyList:
        MonthlyId = Monthly['id']  # 获取id
        # 删除所有的数据
        Wt().delete_monthly(token, MonthlyId)  # 删除日报
    # 专项汇报
    for special in specialList:
        specialId = special['id']  # 获取id
        # 删除所有的数据
        Wt().delete_special(token, specialId)  # 删除日报
    print("删除完成")
    for one in range(1, 7):  # 创建表单测试数据
        Wt().add_Daily(token, add_report(one)[0])  # 日报
        Wt().add_weekly(token, add_report(one)[1])  # 周报
        Wt().add_monthly(token, add_report(one)[2])  # 月报
        Wt().add_special(token, add_report(one)[3])  # 专项汇报
        print("正在添加数据")
    print("测试数据添加完成")

    # 环境、数据清除----teardown
    def fin():

        print('----测试环境恢复----')

    request.addfinalizer(fin)
