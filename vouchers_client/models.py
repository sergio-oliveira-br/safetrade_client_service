# vouchers_client/models.py

# Create your models here.
class Voucher:

    def __init__(self, voucher_id, status, tx_hash=None):
        self.voucher_id = voucher_id
        self.status = status
        self.tx_hash = tx_hash