// vouchers_client/static/vouchers_client/js/web3_wallet_handler.js

const btn  = document.getElementById('connectButton');
const statusSpan = document.getElementById('walletAddress');


async function connect() {
async function connectToMetaMask() {

    if(is_metamask_installed()) {
        try {
            btn.disabled = true;
            btn.innerText = "Connecting...";

            // connect to MetaMask popup
            const accounts = await window.ethereum.request({
            method: 'eth_requestAccounts'
            });

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

btn.onclick = connect;btn.onclick = connectToMetaMask;