
var registry_check_list = [false, false, false, false];

/**
 * Inspektor okna rejestracji
 * @param obj
 */
function Progress(obj) {
    var switcher = obj.name;
    // Sprawdza i ustala które pola zostały wypełnione
    switch (switcher) {
        case 'first_name':
            registry_check_list[0] = obj.value.length > 2 ? true : false;
            break;
        case 'last_name':
            registry_check_list[1] = obj.value.length > 2 ? true : false;
            break;
        case 'email':
            registry_check_list[2] = obj.value.length > 5 ? true : false;
            break;
        case 'pass':
            var len = $('#pass').val();
            len = $('#pass').val() != $('#repeat_pass').val() ? "#FFA58F" : (len.length >= 8 ? "#BBFFB5" : "#FFA58F");
            $('#repeat_pass').css("background-color", len);
            registry_check_list[3] = len != "#FFA58F" ? true : false;
            break;
        case 'repeat_pass':
            var len = $('#repeat_pass').val();
            len = $('#pass').val() != $('#repeat_pass').val() ? "#FFA58F" : (len.length >= 8 ? "#BBFFB5" : "#FFA58F");
            $('#repeat_pass').css("background-color", len);
            registry_check_list[3] = len != "#FFA58F" ? true : false;
            break;
    }
    // Sprawdza czy wszystkie pola zostały wypełnione
    var go_Registry = () => {
        var callback = true;
        registry_check_list.forEach((item, index) => {
            if (item == false) callback = false;
            // log(`Item ${index}: ${item}`)
        });
        return callback;
    }

    // Aktywowanie przycisku rejsetracji po wypełnieniu wszystkich pól
    !go_Registry() ? $("#sub").attr('disabled', 'disabled') : $("#sub").removeAttr('disabled');
}

function get_data_from_ajax(json) {
    log(json[0]);
    if (json[0] == true) {
        showPanel('menu');
    }
    DispalyMessage(json[1]);
    log(json);
}

function SubmitRegistry() {
    DispalyMessage('Trwa rejestracja...');
    var pass1 = $('#pass').val();
    pass1 = CryptoJS.MD5(pass1);
    var pass2 = $('#repeat_pass').val();
    pass2 = CryptoJS.MD5(pass2);
    var send_box = [
        $("#first_name").val(),
        $("#last_name").val(),
        $("#email").val(),
        String(pass1),
        String(pass2)];
    log(send_box);
    simpleAjax(get_data_from_ajax, send_box, 'registry');
    log('Try registry', 'i');
}
