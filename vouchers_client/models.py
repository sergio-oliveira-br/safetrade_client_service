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
