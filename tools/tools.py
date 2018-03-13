import hashlib
from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail


# 哈希校验
def hash_parity(parity, salt='ttsx'):
    parity += salt
    h = hashlib.sha256(parity.encode())
    return h.hexdigest()

# 制作验证码
def make_confirm_code(username):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = hash_parity(username, now)
    return code

# 发送邮件
def send_mail_to_user(email, code, send_type='register'):
    subject = '天天生鲜——注册确认邮件'
    message = '''感谢注册天天生鲜
    请点击 http://{0}/user/confirm/?code={1} 完成注册确认！
    此链接有效期为{2}天！'''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    result = send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
    return result