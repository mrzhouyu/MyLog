# myblog
My forms is created by Django

这是一个Django设计的表单登陆


其中：
  数据库：使用了本地的mysql数据库 详见settings.py 80-89 row
  JS：使用了 Jquery,bootstrap框架 详见static
  验证：使用了163邮箱 smtp  详情settings.py 134-138 row（） 暂无
  加密:hash
  表单：使用了Django自带的 forms 详见forms.py
  验证码：使用了django-simple-captcha==0.5.5 详见forms.py views.py 自动验证与判断 判断.is_valid()方法

