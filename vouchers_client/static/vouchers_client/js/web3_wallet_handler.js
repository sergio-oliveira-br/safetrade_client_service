// vouchers_client/static/vouchers_client/js/web3_wallet_handler.js

window.onload = is_connected;

const btn  = document.getElementById('connectButton');
const statusSpan = document.getElementById('walletAddress');

async function is_connected() {

    const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts'
    });

    const account = accounts[0];
    statusSpan.innerText = "Wallet: " + account;
    btn.disabled = true;
    btn.innerText = "Wallet Connected";
    return true
}


async function connectToMetaMask() {

    if(is_metamask_installed()) {
        try {
            const accounts = await window.ethereum.request({
                method: 'eth_requestAccounts'
            });

            btn.innerText = "Connecting...";
            const account = accounts[0];
            statusSpan.innerText = "Wallet: " + account;
            btn.classList.remove('btn-primary');
            btn.classList.add('btn-success');
            btn.innerText = "Wallet Connected";

            alert("Connected successfully! \nAccount: " + account);

            return true

        } catch (error) {
         alert("User refused the connection." + error);
            btn.disabled = false;
            btn.innerText = "Wallet Connected ";
            console.error("Error :", error);
            return false
        }
    }
}

btn.onclick = connectToMetaMask;