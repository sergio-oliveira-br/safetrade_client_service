// vouchers_client/static/vouchers_client/js/web3_send_tx_hash_to_backend.js

async function sendHashToDjango(tx_hash) {

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const voucher_id = document.getElementById('buy_voucher').getAttribute('data-id');

    try {
        const response = await fetch('/update_voucher_tx_hash/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'tx_hash': tx_hash,
                'voucher_id': voucher_id
            })
        });
        if (response.ok) {
            console.log("Voucher has been updated", response.json())
        }

        if (!response.ok) {
            console.error("Error communicating with Django server.", response.json());
        }
    } catch (error) {
        console.error("Error in Fetch request:", error);
    }
}