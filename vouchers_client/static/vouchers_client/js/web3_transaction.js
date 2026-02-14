// vouchers_client/static/vouchers_client/js/web3_transaction.js

const btn_by_voucher = document.getElementById('buyVoucher')

async function connectWallet() {
    const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts'
    });
    return accounts[0];
}

async function sendTransactionToMetaMask(account) {
    const transactionParameters = {
        from: account,
        to: "0x29E70456ce821A009492FcB44232D67b042a1B49",
        value: "0",
        chainId: "0xaa36a7"
    };

    return await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionParameters]
    });
}

function updateUI(tx_hash) {
    alert("We are processing your payment. Please wait few seconds!");
    console.log("Transaction Hash:", tx_hash);
}

async function buyVoucher() {
    try {
        const account = await connectWallet();
        const tx_hash = await sendTransactionToMetaMask(account);
        updateUI(tx_hash);

        // await sendHashToDjango(tx_hash);

    } catch (error) {
        console.error(error);
        alert("Error: " + error.message);
    }
}

btn_by_voucher.onclick = buyVoucher