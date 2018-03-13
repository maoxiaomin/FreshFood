from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# 用户信息
class UserProfile(AbstractUser):
    nick_name = models.CharField('昵称', max_length=30)
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=6, choices=(('male','男'),('female','女')), default='male')
    address = models.CharField('地址', max_length=100, default='')
    mobile = models.CharField('手机', max_length=11)
    image = models.ImageField('头像', max_length=100, upload_to='head/%Y/%m', default='head/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Mailbox(models.Model):
    user  = models.OneToOneField('UserProfile' , on_delete=models.CASCADE, verbose_name='所属用户')
    code = models.CharField('验证码', max_length=100)
    email = models.EmailField('邮箱', max_length=20)
    type = models.CharField('发送类型', max_length=8, choices=(('register','注册'),('forget', '忘记密码')), default='register')
    send_time = models.DateTimeField('发送时间', default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


