import json

from django.db import models
from boto3.dynamodb.conditions import Key

import boto3
from django.http import JsonResponse


# Create your models here.
class Voucher(models.Model):

    # AWS Details
    _TABLE_NAME = 'vouchers_db'
    _REGION = 'eu-west-1'

    @classmethod
    def _get_table(cls):
        dynamodb = boto3.resource('dynamodb', region_name=cls._REGION)
        return dynamodb.Table(cls._TABLE_NAME)

    @staticmethod
    def list_vouchers_by_status(status_code):
        table = Voucher._get_table()
        response = table.query(
            IndexName='voucher_status_index',
            KeyConditionExpression=Key('voucher_status').eq('Active')
        )

        return response.get('Items', [])

    @staticmethod
    def find_voucher_by_id(voucher_id):
        table = Voucher._get_table()
        response = table.get_item(Key={'voucher_id': voucher_id})
        return response.get('Item', None)


    @staticmethod
    def update_tx_hash(request):

        data = json.loads(request)
        tx_hash = data.get('tx_hash')
        voucher_id = data.get('voucher_id')

        table = Voucher._get_table()
        response = table.update_item(Key={
            'voucher_id':voucher_id },
            UpdateExpression='SET '
                             'voucher_tx_hash = :val_tx_hash',
            ExpressionAttributeValues={
                ':val_tx_hash': tx_hash
            }
        )
        return response