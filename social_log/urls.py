
from django.contrib import admin
from django.urls import path,include
from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("",views.Home,name="home"),
    path("accounts/profile/" ,views.Profile)
]
