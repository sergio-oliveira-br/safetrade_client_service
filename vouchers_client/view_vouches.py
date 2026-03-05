# vouchers_client/view_vouches.py
from django.core.paginator import Paginator
from django.shortcuts import render
from vouchers_client.services.aws_dynamo_service import VoucherDynamoService

def showroom(request):

    voucher_service = VoucherDynamoService()
    vouchers_table_list = voucher_service.list_vouchers_by_status(status='Active')

    paginator = Paginator(vouchers_table_list, 5)
    num_pages = request.GET.get('page')
    page_obj = paginator.get_page(num_pages)

    context = {
        'vouchers_table_list': vouchers_table_list,
        'page_obj': page_obj,
    }
    return render(request, 'core/showroom.html', context)