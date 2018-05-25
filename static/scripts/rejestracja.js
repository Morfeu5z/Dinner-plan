var progresbar = 0;
var passok = false;
var lista = [0, 0, 0, 0];

/**
 * Sprawdzanie okna rejestracji na bierząco
 * Wyświetlanie paska postępu
 * @param input
 */
function progress(input) {
    if (input == 1) {
        if ($("#in1").val() == '') {
            lista[0] = 0;
        } else {
            lista[0] = 25;
        }
    } else if (input == 2) {
        if ($("#in2").val() == '') {
            lista[1] = 0;
        } else {
            lista[1] = 25;
        }
    } else if (input == 3) {
        if ($("#in3").val() == '') {
            lista[2] = 0;
        } else {
            lista[2] = 25;
        }
    } else if (input == 4) {
        if ($("#in4").val() == '') {
            lista[3] = 0;
        } else {
            lista[3] = 25;
        }
    }
    progresbar = lista[0] + lista[1] + lista[2] + lista[3];
    $("#progressbar").width(progresbar + "%");
    console.log("Update progress: " + progresbar);
    $("#progressbar").text(progresbar + "%");

    var len = $('#in3').val();
    if ($('#in3').val() != $('#in4').val()) {
        $('#in4').css("background-color", "#FFA58F");
    }else if(len.length >= 8){
        $('#in4').css("background-color", "#BBFFB5");
    }

    if (progresbar == 100) {
        if ($('#in3').val() == $('#in4').val()) {
            $("#sub").removeAttr('disabled');
            $("#progressbar").text("OK");
        } else {
            $("#sub").attr('disabled', 'disabled');
        }
    } else {
        $("#sub").attr('disabled', 'disabled');
    }
}

/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function log_reg(where) {
    if (where == 'toReg') {
        console.log('Go to reg');
        $("#log").animate({
                opacity: 0,
            }, {
                duration: 1000,
                complete: function () {
                    console.log('Animate half');
                    $("#log").css('display', 'none');
                    $("#reg").css('display', 'block');
                    $("#reg").animate({
                        opacity: '1'
                    }, 1000);
                    console.log('Animate end');
                }
            }
        );

    } else if (where == 'toLog') {
        console.log('Go to log');
        $("#reg").animate({
                opacity: 0,
            }, {
                duration: 1000,
                complete: function () {
                    console.log('Animate half');
                    $("#reg").css('display', 'none');
                    $("#log").css('display', 'block');
                    $("#log").animate({
                        opacity: '1'
                    }, 1000);
                    console.log('Animate end');
                }
            }
        );
    }
}

/**
 * Aktywuje przycisk gdy w inputach jest jakaś wartość
 */
function login() {
    if ($('#inLog').val() != '' && $('#inPass').val() != '') {
        $("#subLogin").removeAttr('disabled');
    } else {
        $("#subLogin").attr('disabled', 'disabled');
    }
}