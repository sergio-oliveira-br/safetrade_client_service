# vouchers_client/view_transaction.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from vouchers_client.services.aws_sqs_service import SQSService
from vouchers_client.services.aws_dynamo_service import VoucherDynamoService

def voucher_checkout_page(request, voucher_id):

    voucher_service = VoucherDynamoService()
    voucher = voucher_service.find_voucher_by_id(voucher_id)

    context = {
        'voucher': voucher
    }
    return render(request, 'core/voucher_checkout.html', context)


@csrf_protect
def update_voucher_with_tx_hash_view(request):

    # Get the Tx Hash from the request and sent to update service method to update the table with that
    voucher_service = VoucherDynamoService()
    voucher_to_update_with_tx_hash = voucher_service.update_voucher_with_tx_hash(request.body)

    is_voucher_success_updated = voucher_to_update_with_tx_hash['success']
    if is_voucher_success_updated:
        if SQSService.send_hash_to_sqs():
            response = JsonResponse({'message': 'Message sent'}, status=200)
        else:
            response = JsonResponse({'message': 'Message not sent'}, status=404)
    else:
        response = JsonResponse({'message': 'Voucher has not been updated' }, status=500)

    return response



