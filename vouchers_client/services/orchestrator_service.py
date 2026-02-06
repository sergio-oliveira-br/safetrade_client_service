# vouchers_client/services/orchestrator_service.py
import json
from venv import logger

from botocore.exceptions import ClientError

from vouchers_client.services.aws_dynamo_service import VoucherDynamoService
from vouchers_client.services.aws_sqs_service import SQSService


class VoucherCheckoutOrchestrator:

    def __init__(self):
        self.db_service = VoucherDynamoService()
        self.sqs_service = SQSService()

    def handle_checkout_update(self, raw_data):
        try:
            raw_data = json.loads(raw_data)
            print(raw_data)

            voucher_id = raw_data.get('voucher_id')
            voucher_tx_hash = raw_data.get('tx_hash')

            if not voucher_tx_hash or not voucher_id:
                return {'success': False,
                        'message': 'Missing voucher_tx_hash or voucher_id',
                        'status_code': 400 }

            # first step: send the tx_hash to dynamodb and change the voucher status
            dynamoDB_response = self.db_service.update_voucher_with_tx_hash(raw_data)

            if not dynamoDB_response['success']:
                return {'success': False,
                        'message': 'It was possible to update the voucher with tx_hash',
                        'status_code': 400 }

            payload = {
                'voucher_id': voucher_id,
                'tx_hash': voucher_tx_hash,
            }

            # send to sqs
            sqs_response = self.sqs_service.push_to_queue(payload)

            if not sqs_response['success']:
                return {'success': False,
                        'message': 'It was possible send the hash to SQS',
                        'status_code': 400 }

            return {'success': True,
                    'message': 'Flow Completed',
                    'message_id': sqs_response.get('message_id'),
                    'status_code': 200}

        except ClientError as e:
            logger.error(f"Unexpected error in the Orchestrator: {e}", exc_info=True)
            return {'success': False,
                    'message': e.response['Error']['Message'],
                    'status_code': 500}