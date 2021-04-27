$(function(){
    eel.expose(change_message)
    function change_message(type, text) {
        const $message = $("#message");

        $message.removeClass("alert-primary");
        $message.removeClass("alert-success");
        $message.removeClass("alert-danger");
        $message.removeClass("alert-secondary");

        if (type === "running") {
            $message.addClass("alert-primary");
        } else if (type === "success") {
            $message.addClass("alert-success");
        } else if (type === "error") {
            $message.addClass("alert-danger");
        } else {
            $message.addClass("alert-secondary");
        }

        $message.text(text)
    }

    eel.expose(change_search_button)
    function change_search_button(is_disable) {
        if (is_disable === "disable") {
            $("#btn-search").prop("disabled", true);
        } else {
            $("#btn-search").prop("disabled", false);
        }
    }

    $("#btn-search").click(() => {
        const searchText = $("#input-search-text").val();
        const count = $("#input-count").val();
        eel.search(searchText, count)
    });
});
