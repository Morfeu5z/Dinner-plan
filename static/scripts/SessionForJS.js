/**
 * Dodanie/Update sesji
 * @param name
 * @param param
 */
function setSession(name, param) {
    $.ajax({
        method: 'POST',
        url: 'sessionControler',
        async: false,
        data: {
            'action': 'set',
            'name': name,
            'param': param,
        },
        success: function (response) {
            console.log("Dodano sesję: " + name + " = " + response.param)
        },
        error: function (error) {
            console.log("Dodanie sesji nie powiodło się.")
        }
    });
}

/**
 * Pobranie sesji
 * @param name
 * @returns {string | null}
 */
function getSession(name) {
        $.ajax({
        method: 'POST',
        url: 'sessionControler',
        async: false,
        data: {
            'action': 'get',
            'name': name,
        },
        success: function (response) {
            console.log("Pobrano sesję: " + name + " = " + response.param);
            localStorage.setItem("param", response.param);
        },
        error: function (error) {
            console.log("Sesja nie istnieje.");
            localStorage.setItem("param", '');
        },
    });
    return localStorage.getItem("param");
}

function clearSession() {
    $.ajax({
        method: 'POST',
        url: 'sessionControler',
        async: true,
        data: {
            'action': 'clear',
        },
        success: function (response) {
            console.log("Result: " + name + " = " + response.param)
        },
        error: function (error) {
            console.log("Sesja nie została wyczyszczona.")
        }
    });
}