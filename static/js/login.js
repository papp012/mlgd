

main();

function main() {
    login();
}

function login() {
    const loginButton = document.querySelector("#send-login-info");
    loginButton.addEventListener('click', sendLoginInfo);
}

async function sendLoginInfo() {
    let loginName = document.querySelector('#login-name');
    let loginEmail = document.querySelector('#login-email');
    let loginPassword1 = document.querySelector('#login-password1');
    let loginPassword2 = document.querySelector('#login-password2');

    if (loginPassword1 === loginPassword2) {
        await apiPost('/api/save-login', {
            loginName: loginName,
            loginEmail: loginEmail,
            loginPassword1: loginPassword1,
            loginPassword2: loginPassword2
        });
    }
    else {
        alert("different passwords!");
    }
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
    return response.json();
}
