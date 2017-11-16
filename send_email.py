#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 11:07
# @Author  : Yu
# @Site    : 
# @File    : send_email.py
import os
from django.core.mail import send_mail
os.environ['DJANGO_SETTINGS_MODULE']='mylog.settings'
if __name__ == '__main__':

    send_mail(
        '来自zhouyu的测试邮件',
        '这是我的邮箱信息',
        '18159851016@163.com',
        ['1078580516@qq.com'],
    )