from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('pricing/', views.pricing, name='pricing'),


]
