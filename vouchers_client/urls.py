# vouchers_client/urls.py
from django.urls import path
from . import view_index, view_checkout, view_vouches

urlpatterns = [
    # Index
    path('', view_index.index_page , name='index'),
    path('showroom/', view_vouches.showroom, name='showroom'),
    path('voucher_checkout/<str:voucher_id>/', view_checkout.voucher_checkout_page, name='voucher_checkout'),
    path('update_voucher_tx_hash/', view_checkout.voucher_checkout_update, name='update_voucher_table'),
]