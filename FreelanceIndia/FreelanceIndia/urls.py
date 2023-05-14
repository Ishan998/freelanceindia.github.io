
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.client.auth,name="mainpage"),
path('addjob',views.client.addproject,name="addjob"),
path('register',views.client.register,name="register"),
path('registercheck',views.client.registercheck,name="registercheck"),
]
