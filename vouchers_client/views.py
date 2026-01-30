from django.shortcuts import render, get_object_or_404

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

def view_voucher_checkout(request, voucher_id):

    voucher = Voucher.find_voucher_by_id(voucher_id)


    context = {
        'voucher': voucher
    }

    return render(request, 'core/voucher_checkout.html', context)
