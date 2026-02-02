from django.db import models
from boto3.dynamodb.conditions import Key

import boto3

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
        response = table.query(KeyConditionExpression=Key('voucher_status').eq(status_code))

        return response.get('Items', [])

    @staticmethod
    def find_voucher_by_id(voucher_id):

        table = Voucher._get_table()

        response = table.get_item(Key={'voucher_status': 'Active' , 'voucher_id': voucher_id})

        return response.get('Item', [])
    @staticmethod
    def update_tx_hash(request):

        table = Voucher._get_table()
        response = table.update_item(Key={
            'voucher_status': 'Active' ,
            'voucher_id':'A9003F19'},
            UpdateExpression='SET tx_hash = :val',
            ExpressionAttributeValues={
                ':val': 'HiSergio2023'
            }
        )
        return response