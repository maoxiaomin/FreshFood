import datetime

from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.conf import settings

from .forms import RegisterForm, LoginForm
from .models import UserProfile, Mailbox
from tools import tools

class CustomBackend(ModelBackend):
    '''
    自定义登录验证
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class RegisterView(View):
    '''
    注册视图
    '''
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        register_form =RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            pwd = register_form.cleaned_data['pwd']
            cpwd = register_form.cleaned_data['cpwd']
            email = register_form.cleaned_data['email']

            if UserProfile.objects.filter(username=username):
                u_msg = '该用户名已被注册'
                return render(request, 'user/register.html', {'u_msg':u_msg, 'register_form':register_form})
            if UserProfile.objects.filter(email=email):
                e_msg = '该邮箱已被注册'
                return render(request, 'user/register.html', {'e_msg': e_msg, 'register_form':register_form})

            if pwd == cpwd:
                new_user = UserProfile()
                new_user.username = username
                new_user.password = make_password(pwd)
                new_user.email = email
                new_user.is_active = False
                new_user.save()
                # 制作校验码
                code = tools.make_confirm_code(username)
                # 发送邮件
                result = tools.send_mail_to_user(email, code)
                if result:
                    # 存储至数据库
                    Mailbox.objects.create(user=new_user, code=code, email=email)
                return render(request, 'user/success.html', {'email':email})

        return render(request, 'user/register.html', {'register_form':register_form})

class LoingView(View):
    '''
    登录视图
    '''
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            pwd = login_form.cleaned_data['pwd']
            user = authenticate(username=username, password=pwd)
            if user is not None:
                if user.is_active:
                    remember = request.POST.get('remember', 0)
                    response = redirect('/')
                    if remember != 0:
                        response.set_cookie('username', username)
                        return response
                    else:
                        response.set_cookie('username', '', max_age=-1)
                        return response
                else:
                    msg = '用户邮箱还未激活！'
                    return render(request, 'user/login.html', {'msg':msg})

            return render(request, 'user/login.html', {'msg':'用户名或密码输入错误！'})
        return render(request, 'user/login.html', {'login_form':login_form})

class ConfirmView(View):
    '''
    激活用户
    '''
    def get(self, request):
        code = request.GET.get('code', '')
        if code:
            try:
                confirm = Mailbox.objects.get(code=code)
            except:
                msg = '无效的注册码！'
                return render(request, 'user/confirm.html', {'msg':msg})
            else:
                send_time = confirm.send_time
                now = datetime.datetime.now()
                if now > send_time + datetime.timedelta(settings.CONFIRM_DAYS):
                    confirm.user.delete()
                    confirm.delete()
                    msg = '邮件已经过期，原用户已失效，请重新注册！'
                    return render(request, 'user/confirm.html', {'msg':msg})
                else:
                    confirm.user.is_active = True
                    confirm.user.save()
                    confirm.delete()
                    msg = '感谢确认, 请使用该账户登录！'
                    return render(request, 'user/success.html', {'msg': msg})
        else:
            msg = '您的链接不正确！'
            return render(request, 'user/confirm.html', {'msg': msg})

class UserCenterInfoView(View):
    def get(self, request):
        active = 'info'
        return render(request, 'user/user_center_info.html',{'active':active})

class UserCenterOrderView(View):
    def get(self, request):
        active = 'order'
        return render(request, 'user/user_center_order.html', {'active':active})