"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from users import views as user_views 
from django.contrib.auth import views as auth_views #for login and logout 
from django.conf import settings #copied from django website
from django.conf.urls.static import static #copeid from django website

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #class based views 
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), #class based views
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'), #class based views
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'), #class based views
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'), #class based views
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'), #class based views
    path('',include('blog.urls')), #this takes to the urls.py of the blog folder
]

#copied and pasted from Django website 
#for handling media. Notice this is added to the list of url patterns from above
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)