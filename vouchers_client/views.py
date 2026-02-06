from django.shortcuts import render
from vouchers_client.aws_dynamo_service import VoucherDynamoService


# Create your views here.
def index_page(request):
    return render(request, 'core/index.html')

def showroom(request):

    voucher_service = VoucherDynamoService()
    vouchers_table_list = voucher_service.list_vouchers_by_status(status='Active')

    context = {
        'vouchers_table_list': vouchers_table_list,
    }
    return render(request, 'core/showroom.html', context)


