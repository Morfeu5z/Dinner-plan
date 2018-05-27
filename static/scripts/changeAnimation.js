/**
 * Animacja przejścia między rejestracją, a logowaniem
 * @param where
 */
function showPanel(where) {
    console.log('Go to: ' + where);
    $("#include").animate({
            opacity: 0,
        }, {
            duration: 500,
            complete: function () {
                console.log('Animate half');
                $("#include").load("/include_"+where, function () {
                    $("#include").animate({
                        opacity: '1'
                    }, 500);
                });
                console.log('Animate end');
            }
        }
    );
}
