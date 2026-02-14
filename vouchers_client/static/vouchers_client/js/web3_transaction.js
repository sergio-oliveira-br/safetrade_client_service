// vouchers_client/static/vouchers_client/js/web3_transaction.js

const btn_by_voucher = document.getElementById('buyVoucher')
const btn_check_tx = document.getElementById('checkTx')
const paymentStatus = document.getElementById("paymentStatus");

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

    // update the UI
    paymentStatus.innerText = 'Waiting for confirmation'

    return await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionParameters]
    });
}

function updateUI(tx_hash) {
    alert("Your payment has been successfully recorded in Etherscan!");
    console.log("Transaction Hash:", tx_hash);
    btn_by_voucher.style.display = 'none';
    btn_check_tx.style.display = 'Block';

    const txDisplay = document.getElementById("tx_hash_display");
    const txInput = document.getElementById("tx_hash_input");
    paymentStatus.innerText = 'Transaction recorded in Etherscan'

    if (txDisplay) txDisplay.innerText = tx_hash;
    if (txInput) txInput.value = tx_hash;
}

async function buyVoucher() {
    try {
        const account = await connectWallet();
        const tx_hash = await sendTransactionToMetaMask(account);
        updateUI(tx_hash);

    } catch (error) {
        console.error(error);
        alert("Error: " + error.message);
    }
}

btn_by_voucher.onclick = buyVoucher