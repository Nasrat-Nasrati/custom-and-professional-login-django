from django import forms
# from captcha.fields import ReCaptchaField
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}),
        }
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # اینجا اعتبارسنجی پیش‌فرض username را حذف کردیم (هر مقداری را قبول می‌کند)
        return username

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
