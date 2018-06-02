/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function showPanel(where) {
    log(where, 'gt');
    $("#include").animate({
            opacity: 0,
        }, {
            duration: 500,
            complete: function () {
                $("#include").load("/include_" + where, function () {
                    $("#include").animate({
                        opacity: '1'
                    }, 500);
                });
                log(where, 'l');
                localStorage.setItem('where', where);
            }
        }
    );
}