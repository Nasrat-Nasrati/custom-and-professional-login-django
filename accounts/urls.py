from django.urls import path
from .views import signup_view, login_view
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import logout_view
from . import views


app_name = 'accounts'

urlpatterns = [
    # صفحات عمومی
    path('contact/', views.contact_view, name='contact'),
    path('home/',views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('news/', views.news_view, name='news'),

    # صفحات محافظت‌شده
    path('students/', views.students_view, name='students'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('courses/', views.courses_view, name='courses'),

    # احراز هویت
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
