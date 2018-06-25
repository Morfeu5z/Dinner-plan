function DispalyMessage(message, timer, id) {
    $("#" + id).html("" +
        "<div " +
        "id='display_popup_who_was_created' " +
        "style=\"" +
        "position: fixed; " +
        "width: auto; " +
        "height: auto; " +
        "padding: 15px 25px;" +
        "background: #ddeaff; " +
        "top: 5px;" +
        "right: 0px;" +
        "font-size: 1rem;" +
        "max-width: 40vw;" +
        "z-index: 10;" +
        "background: #fff;" +
        "box-shadow: 1px 1px 5px rgba(0,0,0,0.5);" +
        "text-shadow: 1px 1px 3px rgba(0,0,0,0.3);" +
        "word-wrap: break-word;" +
        "text-align: right;" +
        "font-family:  'Lucida Grande', 'Lucida Sans Unicode', 'Geneva', 'Verdana', sans-serif" +
        "\">" +
        "" + message +
        "</div>");
    var pop = document.getElementById('display_popup_who_was_created');
    var pop_right = pop.offsetWidth * -1;
    $("#display_popup_who_was_created").css("right", pop_right);
    $("#display_popup_who_was_created").animate({right: '0px'}).delay(timer);
    $("#display_popup_who_was_created").animate({right: pop_right + 'px'}, {
        complete: function () {
            $("#display_popup_who_was_created").css("display", "none");
        }
    });
}