from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
  path("",views.index,name="Home"),
  path("login",views.loginuser,name="login"),
  path("logout",views.logoutuser,name="logout")
]
