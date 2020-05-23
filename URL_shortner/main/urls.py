from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', views.home, name='home'),
  url(r'//(\w+)/', views.red, name='home'),
  url(r'^f/(\w+)/', views.red, name='home2'),
  url(r'^cust/(\w+)/', views.cust, name='home2'),
  url(r'^short/', views.short, name='home2')
]
