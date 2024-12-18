from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from django.db import IntegrityError
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.hashers import make_password  # Dùng để mã hóa mật khẩu

from django.utils import timezone

from django.urls import reverse

from .models import *

def Home(request):
    return render(request, 'index.html')

def LoginView(request):
    return render(request, 'login.html')

def RegisterView(request):
    errors = {}  # Dictionary để lưu lỗi

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        agree_terms = request.POST.get('agree_terms') == 'on'

        # Kiểm tra email
        try:
            validate_email(email)
        except:
            errors['email'] = "Email không hợp lệ. Vui lòng nhập lại."

        # Regex email kiểm tra bổ sung
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            errors['email'] = "Email không hợp lệ. Vui lòng nhập lại."

        # Kiểm tra mật khẩu khớp
        if password != confirm_password:
            errors['confirm_password'] = "Mật khẩu xác nhận không khớp."

        # Kiểm tra độ mạnh mật khẩu
        if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            errors['password'] = "Mật khẩu phải chứa ít nhất 8 ký tự, gồm chữ hoa, chữ thường và số."

        # Kiểm tra số điện thoại
        if not phone or not re.match(r'^0[0-9]{9,10}$', phone):
            errors['phone'] = "Số điện thoại không hợp lệ. Vui lòng nhập lại."

        # Kiểm tra xem email và số điện thoại đã tồn tại chưa
        if UserProfile.objects.filter(email=email).exists():
            errors['email'] = "Email đã được sử dụng."
        if UserProfile.objects.filter(phone=phone).exists():
            errors['phone'] = "Số điện thoại đã được sử dụng."

        # Kiểm tra điều khoản
        if not agree_terms:
            errors['agree_terms'] = "Bạn cần đồng ý với các điều khoản sử dụng."

        # Nếu không có lỗi, lưu dữ liệu
        if not errors:
            user_profile = UserProfile(
                email=email,
                password=make_password(password),
                phone=phone,
                city=city,
                agree_terms=agree_terms
            )
            user_profile.save()
            return redirect('login')  # Chuyển đến trang đăng nhập

    # Truyền form data và lỗi về template
    return render(request, 'register.html', {'errors': errors, 'data': request.POST})

def WhyPage(request):
    return render(request,"why.html")

def AboutPage(request):
    return render(request,"about.html")

def TeamPage(request):
    return render(request,"team.html")

def ServicePage(request):
    return render(request,"service.html")