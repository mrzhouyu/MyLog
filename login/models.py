from django.db import models

# Create your models here.
class User(models.Model):
    gender=(
        ('male',"男"),
        ('femals',"女"),    )
    # name必填，最长不超过128个字符，并且唯一，也就是不能有相同姓名；
    # password必填，最长不超过256个字符（实际可能不需要这么长）；
    # email使用Django内置的邮箱类型，并且唯一；
    # 性别使用了一个choice，只能选择男或者女，默认为男；
    name=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)
    email=models.EmailField(unique=True)
    sex=models.CharField(max_length=32,choices=gender,default='男')
    c_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    #设置元信息 db_table定义数据表名称 ordering 排序 这个类是用来设置自定义的  不然就是默认
    class Meta:
        #加-表示倒序
        ordering=["-c_time"]
        verbose_name="用户"
        verbose_name_plural="用户"

