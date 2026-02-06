import json
from venv import logger

import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
from django.http import JsonResponse


class VoucherDynamoService:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
        self.table = self.dynamodb.Table('vouchers_db')


    def list_vouchers_by_status(self, status):
        response = self.table.query(
            IndexName='voucher_status_index',
            KeyConditionExpression=Key('voucher_status').eq(status)
        )
        return response.get('Items', [])


    def find_voucher_by_id(self, voucher_id):
        response = self.table.get_item(Key={'voucher_id': voucher_id})
        return response.get('Item', None)


    def update_transaction_with_tx_hash(self, request):
        # extracting the data
        data_request = json.loads(request)
        tx_hash = data_request.get('tx_hash')
        voucher_id = data_request.get('voucher_id')

        # validations
        if voucher_id is None:
            return JsonResponse({'message': 'voucher_id is required'}, status=422)

        if tx_hash is None:
            return JsonResponse({'message': 'tx_hash is required'}, status=422)

        # updating
        try:
            response = self.table.update_item(
                Key={'voucher_id': voucher_id},
                UpdateExpression='SET '
                                 'voucher_tx_hash = :val_tx_hash,'
                                 'voucher_status = :val_status',
                ExpressionAttributeValues={
                    ':val_tx_hash': tx_hash,
                    ':val_status': 'Pending'
                },
                ReturnValues='UPDATED_NEW'
            )
            return {"success": True, "data": response.get('Attributes')}

        except ClientError as e:
            logger.error(f"Erro AWS: {e}")
            return {"success": False, "error": "Communication Error"}