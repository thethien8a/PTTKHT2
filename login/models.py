from django.db import models

class UserProfile(models.Model):
    email = models.EmailField(unique=True)  # Trường email duy nhất
    password = models.CharField(max_length=255)  # Mật khẩu đã mã hóa
    phone = models.CharField(max_length=15)  # Số điện thoại
    city = models.CharField(max_length=50)  # Thành phố
    agree_terms = models.BooleanField(default=False)  # Đồng ý điều khoản

    def __str__(self):
        return self.email
