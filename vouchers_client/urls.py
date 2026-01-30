# vouchers_client/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Index
    path('', views.index_page , name='index'),
    path('showroom/', views.showroom, name='showroom'),
    path('voucher_checkout/<str:voucher_id>/', views.view_voucher_checkout, name='voucher_checkout'),
]