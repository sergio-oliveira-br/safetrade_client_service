
const btn_by_voucher = document.getElementById('buy_voucher')

async function buy_voucher() {

    const metamask_provider = window.ethereum

    if(await is_connected()) {
        try {
            const accounts = await metamask_provider.request({
                method: 'eth_requestAccounts'
            });

            const account = accounts[0]

            // https://docs.metamask.io/wallet/reference/provider-api#disconnect
            const transactionParameters = {
                from: account,
                to: "0x29E70456CE821A009492FCB44232D67b042A1B49",
                value: "0",
                chainId: "0xaa36a7"
            }
            const tx_hash = await metamask_provider.request({
                method: "eth_sendTransaction",
                params: [transactionParameters]
            });

            alert("tx_hash: " + tx_hash)

            await sendHashToDjango(tx_hash)

        } catch (error) {
            console.error(error)
            alert("Erro: " + error.message)
        }
    } else {
        alert("Please connect to your MetaMask Account before attempt to buy a voucher")
    }
}

btn_by_voucher.onclick = buy_voucher