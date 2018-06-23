var list = [false, false, false, false];

/**
 * Inspektor okna rejestracji
 * @param obj
 */
function progress(obj) {
    var switcher = obj.name;
    // Sprawdza i ustala które pola zostały wypełnione
    switch (switcher) {
        case 'first_name':
            list[0] = obj.value.length > 2 ? true : false;
            break;
        case 'last_name':
            list[1] = obj.value.length > 2 ? true : false;
            break;
        case 'email':
            list[2] = obj.value.length > 5 ? true : false;
            break;
        case 'pass':
            var len = $('#pass').val();
            len = $('#pass').val() != $('#repeat_pass').val() ? "#FFA58F" : (len.length >= 8 ? "#BBFFB5" : "#FFA58F");
            $('#repeat_pass').css("background-color", len);
            list[3] = len != "#FFA58F" ? true : false;
            break;
        case 'repeat_pass':
            var len = $('#repeat_pass').val();
            len = $('#pass').val() != $('#repeat_pass').val() ? "#FFA58F" : (len.length >= 8 ? "#BBFFB5" : "#FFA58F");
            $('#repeat_pass').css("background-color", len);
            list[3] = len != "#FFA58F" ? true : false;
            break;
    }
    // Sprawdza czy wszystkie pola zostały wypełnione
    var go_Registry = () => {
        var callback = true;
        list.forEach((item, index) => {
            if (item == false) callback = false;
            // log(`Item ${index}: ${item}`)
        });
        return callback;
    }

    // Aktywowanie przycisku rejsetracji po wypełnieniu wszystkich pól
    !go_Registry() ? $("#sub").attr('disabled', 'disabled') : $("#sub").removeAttr('disabled');
    $("#sub").removeAttr('disabled');
}

function submit_registry() {
    var send_box = [];
    send_box.push($("#first_name").val()),
    send_box.push($("#last_name").val()),
    send_box.push($("#email").val()),
    send_box.push($("#pass").val()),
    send_box.push($("#repeat_pass").val());
    // log(send_box, 'i');
    var registry_callback = simpleAjax(send_box, 'registry');
}