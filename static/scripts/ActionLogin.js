
var login_check_list = [false, false];

$('#test').bind("click", function () {
    showPanel('menu');
})

function SignInMe(obj) {
    var switcher = obj.name;
    // Sprawdza i ustala które pola zostały wypełnione
    switch (switcher) {
        case 'email':
            login_check_list[0] = obj.value.length > 5 ? true : false;
            break;
        case 'pass':
            var len = $('#pass').val();
            login_check_list[1] = obj.value.length > 5 ? true : false;
            break;
    }
    // Sprawdza czy wszystkie pola zostały wypełnione
    var go_login = () => {
        var callback = true;
        login_check_list.forEach((item, index) => {
            if (item == false) callback = false;
            // log(`Item ${index}: ${item}`)
        });
        return callback;
    }

    // Aktywowanie przycisku rejsetracji po wypełnieniu wszystkich pól
    !go_login ? $("#sign_in").attr('disabled', 'disabled') : $("#sign_in").removeAttr('disabled');
}