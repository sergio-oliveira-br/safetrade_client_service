# vouchers_client/view_vouches.py

from django.shortcuts import render
from vouchers_client.services.aws_dynamo_service import VoucherDynamoService

def showroom(request):
    voucher_service = VoucherDynamoService()
    vouchers_table_list = voucher_service.list_vouchers_by_status(status='Active')

    context = {
        'vouchers_table_list': vouchers_table_list,
    }
    return render(request, 'core/showroom.html', context)


