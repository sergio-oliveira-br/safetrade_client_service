// vouchers_client/static/vouchers_client/js/web3-handler.js

const btn  = document.getElementById('connectButton');
const statusSpan = document.getElementById('walletAddress');

// 2. Função principal de conexão
async function connect() {

    // We check if MetaMask is installed
    if (typeof window.ethereum !== 'undefined') {

        try {

            btn.disabled = true;
            btn.innerText = "Connecting...";

            // connect to MetaMask poopup
            const accounts = await window.ethereum.request({
            method: 'eth_requestAccounts'
            });

            const account = accounts[0];

            statusSpan.innerText = "Wallet: " + account;

            btn.classList.remove('btn-primary');
            btn.classList.add('btn-success');
            btn.innerText = "Wallet Connected";

            alert("Connected successfully! \nAccount: " + account);

        } catch (error) {
         alert("User refused the connection." + error);
            btn.disabled = false;
            btn.innerText = "Wallet Connected ";
            console.error("Error :", error);
        }
    } else {
    alert("MetaMask not detected! Please install the extension.");
    }
}

btn.onclick = connect;