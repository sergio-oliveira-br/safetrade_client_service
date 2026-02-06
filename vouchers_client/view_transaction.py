# vouchers_client/view_transaction.py
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from vouchers_client.services.aws_sqs_service import SQSService
from vouchers_client.services.aws_dynamo_service import VoucherDynamoService
from vouchers_client.services.orchestrator_service import VoucherCheckoutOrchestrator


def voucher_checkout_page(request, voucher_id):

    voucher_service = VoucherDynamoService()
    voucher = voucher_service.find_voucher_by_id(voucher_id)

    context = {
        'voucher': voucher
    }
    return render(request, 'core/voucher_checkout.html', context)


@csrf_protect
def voucher_checkout_update(request):
    # Instantiate the Orchestrator Service
    orchestrator_service = VoucherCheckoutOrchestrator()

    # Use the instance to handle the business logic
    response = orchestrator_service.handle_checkout_update(request.body)
    status_code = 200 if response['status_code'] else 400

    return JsonResponse(response, status=status_code)
