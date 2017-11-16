#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 19:32
# @Author  : Yu
# @Site    : 
# @File    : forms.py
from django import forms
from captcha.fields import CaptchaField
class Myclass(forms.Form):
    username=forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captch=CaptchaField(label="验证码")

class Register(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label="邮箱",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex=forms.ChoiceField(label='性别',choices=gender)
    captcha=CaptchaField(label='验证码')
