from django.shortcuts import render

from vouchers_client.models import Voucher


# Create your views here.
def index_page(request):
    return render(request, 'core/index.html')

def showroom(request):

    vouchers_table_list = Voucher.list_vouchers_by_status('Active')

    context = {
        'vouchers_table_list': vouchers_table_list,
    }
    return render(request, 'core/showroom.html', context)

def payment_processing_view(request):
    return render(request, 'core/payment_processing.html')
