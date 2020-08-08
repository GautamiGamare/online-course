"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='main'),
    path('login_check/',views.login_check,name='login_check'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_welcome/',views.admin_welcome,name='admin_welcome'),
    path('add_new_class/',views.add_new_class,name='add_new_class'),
    path('view_classes/',views.view_classes,name='view_classes'),
    path('save_course/',views.save_course,name='save_course'),
    path('update<int:pk>/',views.update.as_view(),name='update'),
    path('delete/',views.delete,name='delete'),

    path('student/',views.student,name='student'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_regis/',views.student_regis,name='student_regis'),
    path('save_student/',views.save_student,name='save_student'),
    path('student_welcome/',views.student_welcome,name='student_welcome'),
    path('entrol_course/',views.entrol_course,name='entrol_course'),
    path('view_entrolled_courses/',views.view_entrolled_courses,name='view_entrolled_courses'),
    path('cancel_entrolled_courses/',views.cancel_entrolled_courses,name='cancel_entrolled_courses'),
    path('entrol/',views.entrol,name='entrol'),
    path('delete_course/',views.delete_course,name='delete_course'),
    path('contact/',views.contact,name='contact'),
    path('student_logout/',views.student_logout,name='student_logout'),

    path('check_number/',views.check_number,name='check_number'),
    path('check_email/',views.check_email,name='check_email'),
    path('check_cname/',views.check_cname,name="check_cname"),
]
