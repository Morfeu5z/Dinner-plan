var login_check_list = [false, false];

$('#test').bind("click", function () {
    showPanel('menu');
})

function runPassChecker(obj) {
    var switcher = obj.name;
    // log(switcher);
    // Sprawdza i ustala które pola zostały wypełnione
    switch (switcher) {
        case 'email':
            login_check_list[0] = obj.value.length > 5 ? true : false;
            break;
        case 'pass':
            login_check_list[1] = obj.value.length > 5 ? true : false;
            break;
    }
    // Sprawdza czy wszystkie pola zostały wypełnione
    var go_login = login_check_list[0] && login_check_list[1] ? true : false;

    // Aktywowanie przycisku logowania po wypełnieniu wszystkich pól
    !go_login ? $("#sign_in").attr('disabled', 'disabled') : $("#sign_in").removeAttr('disabled');
}


function CheckLoginWithAjax() {
    log('Check login', 'i');
    var pass = $('#pass').val();
    var hash_pass = CryptoJS.MD5(pass);
    var login_data = [$('#email').val(), String(hash_pass)];
    var status = simpleAjax(login_data, 'tryLogin');
    if (status == undefined) {
        DispalyMessage('Bład połączenia, spróbuj zalogować się raz jeszcze.')
    } else {
        DispalyMessage('Logowanie powiodło się.')
    }
    log(status, 'i');
}