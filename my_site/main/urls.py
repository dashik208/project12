from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('mainpage', views.mainpage),
    path('mainpage1', views.mainpage1),
    path('myvisits', views.myvisits),
    path('myfavorites', views.myfavorites),
    path('search', views.search),
    path('account', views.account),
    path('mylink', views.mylink),
    path('myimpressions', views.myimpressions),
]
from django.urls import path, include
urlpatterns = [
 path('users', include('users.urls')),
 path('account', include('django.contrib.auth.urls')),
 ] # Встроенные маршруты для логина/логаута

from django.urls import path
from . views import CustomLoginView
urlpatterns = [
 path('login/', CustomLoginView.as_view(), name='custom_login'),
]
