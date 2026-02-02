# vouchers_client/view_transaction.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from vouchers_client.models import Voucher

def view_voucher_checkout(request, voucher_id):
    voucher = Voucher.find_voucher_by_id(voucher_id)
    context = {
        'voucher': voucher
    }
    return render(request, 'core/voucher_checkout.html', context)


@csrf_protect
def update_voucher_table(request):

    service = Voucher.update_tx_hash(request.body)

    if service:
        response = JsonResponse({'message': 'Voucher updated successfully',}, status=200)
    else:
        response = JsonResponse({'message': 'Voucher update failed'}, status=500)

    return response



