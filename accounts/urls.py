from django.urls import path, include
from . import views
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('verifyOTP', views.verifyOTP, name='verifyOTP' ),
    path('<slug:user_name>', views.userpage, name='userpage'),
]
