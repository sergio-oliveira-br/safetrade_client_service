# vouchers_client/services/aws_sqs_service.py

import json
import logging
import boto3

# AWS Details
REGION = 'eu-west-1'
SQS_QUEUE_URL = 'https://sqs.eu-west-1.amazonaws.com/542672133770/payment-processing-queue'
client = boto3.client('sqs', region_name=REGION)

class SQSService:

    @staticmethod
    def send_hash_to_sqs() -> bool | None:

        if not client:
            logging.error('The message can not be delivered, no SQS client configured')
            return False

        message_payload = {
            'tx_hash': '0x999ab5ee766042609d931158bb28857b019e4cff3ebc787fb07228b747f25b9f'
        }

        try:
            sqs_response = client.send_message(
                QueueUrl=SQS_QUEUE_URL,
                MessageBody=json.dumps(message_payload)
            )
            return True

        except Exception as e:
            logging.error(e)
            return False