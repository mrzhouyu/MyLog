#encoding='utf8'
from django.shortcuts import render,redirect
from django.http import HttpResponse
from login.models import *
from login.forms import Myclass,Register
import hashlib
# Create your views here.
# '''
# 首页
# 登陆
# 注册
# 退出
# '''
def hash_code(s,salt='login'):#这里加点盐  也就是一个用来增加加密安全性的字符串 随便什么都可以
    h=hashlib.sha256()
    s=s+salt
    h.update(s.decode())#update方法只接受bytes类型
    return h.hexdigest()

def index(request):
    return render(request,'login/index.html')
#验证登陆密码 数据库比对
def login(request):
    #这个if通过session来判断判断是否重复登陆 没有这个session key则为None 是的话重定向回index页面 (return后面的语句不会再执行)
    if request.session.get('is_login',None):
        return redirect('/index/')

    if request.method=='POST':
        login_form=Myclass(request.POST)
        # username=request.POST.get("username",None)
        # password=request.POST.get("password",None)
        message="所有字段必须填写"
        # 这个if是验证 包括验证不为空 还有验证码也一并验证了
        if login_form.is_valid():
            # 这里是验证方式 去除字符串开头或者结尾为空格 的情况
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            # username=username.strip()
            try:
                user = User.objects.get(name=username)
                if user.password == password: # 哈希值和数据库内的值进行比对
                    request.session['is_login']=True
                    request.session['user_id']=user.id
                    request.session['user_name']=user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确"
            except:
                message="用户名不存在"
        return render(request, 'login/login.html',locals())
    login_form=Myclass()
    # locals()是python的内置函数 返回当前所有变量的字典 如{'message':message, 'login_form':login_form} 偷懒
    return render(request,'login/login.html',locals())

#注册
def register(request):
    if request.session.get('is_login',None):
        #如果登陆状态则不允许注册
        return redirect('/index/')
    if request.method=='POST':
        register_form=Myclass(request.POST)
        message="请检查填写的内容"
        if register_form.is_valid():#这个判断是验证数据 下面是获取数据
            username=register_form.cleaned_data['username']
            password1=register_form.cleaned_data['password1']
            password2=register_form.cleaned_data['password2']
            email=register_form.cleaned_data['email']
            sex=register_form.cleaned_data['sex']
            if password1!=password2:
                message="两次输入的密码不同"
                return render(request,'login/register.html',locals())
            else:
                same_name_user=User.objects.filter(name=username)
                if same_name_user:
                    message="该用户已经注册，请重新注册"
                    return render(request, 'login/register.html', locals())
                same_email_user=User.objects.filter(email=email)
                if same_email_user:
                    message="该邮箱已经注册，请重新注册"
                    return render(request, 'login/register.html', locals())

                #当所有要求符合时候 创建新的用户
                new_user=User.objects.create()
                new_user.name=username
                new_user.password=password1#加密
                new_user.email=email
                new_user.sex=sex
                new_user.save()
                return redirect('/login/')#自动跳转到登陆页面
    redirect_form=Register()
    return render(request,'login/register.html',locals())
#登出
def logout(request):
    #如果本来就没有登陆 那也就不用登出
    if not request.session.get('is_login',None):
        return redirect('/index/')
    #删除所有会话 则表示登出 如果不需要删除所有 则可以# del request.session['is_login']这样的方法逐一删除
    request.session.flush()
    return redirect('/index/')