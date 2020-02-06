from django.contrib import admin
from django.urls import path
from blog_app import views as b_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', b_v.index),
    path('addblog', b_v.create_blog),
]