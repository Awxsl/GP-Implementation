document.getElementById('username').addEventListener('blur', validateName);
document.getElementById('password').addEventListener('blur', validatePassword);


function validateName() {
    const name = document.getElementById('username');
    const re = /^[A-Za-z0-9]{4,10}$/;

    if(!re.test(name.value)) {
        name.classList.add('is-invalid');
    } else {
        name.classList.remove('is-invalid');
        name.classList.add('is-valid');
    }
}

function validatePassword() {
    const zip = document.getElementById('password');
    const re = /^[a-zA-Z0-9!@#$$%^&*]{6,14}$/;

    if(!re.test(zip.value)) {
        zip.classList.add('is-invalid');
    } else {
        zip.classList.remove('is-invalid');
        zip.classList.add('is-valid');
    }
}
