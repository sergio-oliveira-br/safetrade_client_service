// vouchers_client/static/vouchers_client/js/web3_transaction.js

const btn_by_voucher = document.getElementById('buy_voucher')

async function buy_voucher() {
    try {
        const accounts = await window.ethereum.request({
            method: 'eth_requestAccounts'
        });
        const account = accounts[0];

        // https://docs.metamask.io/wallet/reference/provider-api#disconnect
        const transactionParameters = {
            from: account,
            to: "0x29E70456ce821A009492FcB44232D67b042a1B49",
            value: "0",
            chainId: "0xaa36a7"
        }
        const tx_hash = await window.ethereum.request({
            method: "eth_sendTransaction",
            params: [transactionParameters]
        });

        alert("tx_hash: " + tx_hash)
        await sendHashToDjango(tx_hash)

    } catch (error) {
        console.error(error)
        alert("Erro: " + error.message)
    }
}

btn_by_voucher.onclick = buy_voucher