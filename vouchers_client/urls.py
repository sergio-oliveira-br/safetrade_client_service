# vouchers_client/urls.py
from django.urls import path
from . import views, view_transaction

urlpatterns = [
    # Index
    path('', views.index_page , name='index'),
    path('showroom/', views.showroom, name='showroom'),
    path('voucher_checkout/<str:voucher_id>/', view_transaction.voucher_checkout_page, name='voucher_checkout'),
    path('update_voucher_tx_hash/', view_transaction.update_voucher_with_tx_hash_view, name='update_voucher_table'),
]