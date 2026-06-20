from django.contrib import admin
from django.urls import path
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.quiz_home, name='quiz_home'),
    path('register/', views.register_page, name='register'), # New Registration Link
    path('login/', views.login_page, name='login'),          # New Login Link
    path('logout/', views.logout_user, name='logout'),       # New Logout Link
    path('dashboard/', views.dashboard, name='dashboard'),
]