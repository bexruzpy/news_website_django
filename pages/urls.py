from django.urls import include, path
from .views import home, about, today, yesterday
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel uchun URL
    path("", home, name="home"),
    path("about", about, name="about"),
    path("today", today, name="today"),
    path("yesterday", yesterday, name="yesterday"),
]


