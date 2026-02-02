// vouchers_client/static/vouchers_client/js/metamask_checker.js

function is_metamask_installed() {

    if (typeof window.ethereum === 'undefined') {
        alert("MetaMask not detected! Please install the extension.");
        return false
    }
}