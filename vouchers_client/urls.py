# vouchers_client/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index_page , name='index'),
    path('showroom/', views.showroom, name='showroom'),
]