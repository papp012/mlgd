

main();

function main() {
    login();
}

function login() {
    const loginButton = document.querySelector("#send-login-info");
    loginButton.addEventListener('click', async()=> {
        let loginName = document.querySelector('#login-name').value;
        let loginEmail = document.querySelector('#login-email').value;
        let loginPassword1 = document.querySelector('#login-password1').value;
        let loginPassword2 = document.querySelector('#login-password2').value;

        await apiPost('/api/save-login', {loginName: loginName, loginEmail: loginEmail, loginPassword1:loginPassword1})
    });
}



async function apiPost(url, payload) {
    let response = await fetch(url, {
        method: "POST",
        headers: {
        'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
        body: JSON.stringify(payload)
    });
    //return response.json();
}
