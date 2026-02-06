# vouchers_client/services/aws_sqs_service.py

import json
import logging
import boto3

class SQSService:

    def __init__(self):
        self.sqs_client = boto3.client('sqs', region_name='eu-west-1')
        self.queue_url = 'https://sqs.eu-west-1.amazonaws.com/542672133770/payment-processing-queue'


    def push_to_queue(self, payload: dict):
        try:
            sqs_response = self.sqs_client.send_message(QueueUrl=self.queue_url,
                                                        MessageBody=json.dumps(payload),
                                                        DelaySeconds=30)
            return {'success': True,
                    'message_id': sqs_response.get('MessageId') }

        except Exception as e:
            logging.error(f"Error while sending to queue: {str(e)}", exc_info=True)
            return {'success': False,
                    'error': str(e)}