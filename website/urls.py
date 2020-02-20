from django.contrib import admin
from django.urls import path,include,re_path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('userregister/',views.userregister,name="userregister"),
    path('dnt_send_sms/',views.send_sms_dnt,name="dnt_sms"),
    path('dmt_send_sms/',views.send_sms_dmt,name="dmt_sms"),
    path('dntregister/',views.dntregister,name="dnt_register"),
    path('dmtregister/',views.dmtregister,name="dmt_register"),
   # path('userlogin/',views.userlogin),
    path('usersign_in/',views.usersignin,name='usersign_in'),
    path('dntsign_in/',views.dntsignin,name='dntsign_in'),
    path('dmtsign_in/',views.dmtsignin,name='dmtsign_in'),
    path('userprofile/',views.userprofile,name="userprofile"),
    path('dntprofile/',views.dntprofile,name="dmt_profile"),
    path('dmtprofile/',views.dmtprofile,name="dnt_profile"),
    re_path(r'^loginuser/$',LoginView.as_view(template_name='userlogin.html',redirect_field_name='next'),name='userlogin'),
    re_path(r'^logindnt/$',LoginView.as_view(template_name='dntlogin.html',redirect_field_name='next'),name='dntlogin'),
    re_path(r'^logindmt/$',LoginView.as_view(template_name='dmtlogin.html',redirect_field_name='next'),name='dmtlogin'),
    re_path(r'^logout/$',LogoutView.as_view(next_page="home"),name='logout'),

]