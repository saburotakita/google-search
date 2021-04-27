$(function(){
    // メッセージを変更する
    eel.expose(change_message)
    function change_message(type, text) {
        const $message = $("#message");

        // 現在のクラスを削除
        $message.removeClass("alert-primary");
        $message.removeClass("alert-success");
        $message.removeClass("alert-danger");
        $message.removeClass("alert-secondary");

        // 指定されたクラスをセット
        if (type === "running") {
            $message.addClass("alert-primary");
        } else if (type === "success") {
            $message.addClass("alert-success");
        } else if (type === "error") {
            $message.addClass("alert-danger");
        } else {
            $message.addClass("alert-secondary");
        }

        // メッセージの内容を変更
        $message.text(text)
    }

    // 検索ボタンの有効化、無効化変更
    eel.expose(change_search_button)
    function change_search_button(state) {
        if (state === "disable") {
            $("#btn-search").prop("disabled", true);
        } else {
            $("#btn-search").prop("disabled", false);
        }
    }

    // 検索ボタンのクリック処理
    $("#btn-search").click(() => {
        const searchText = $("#input-search-text").val();
        const count = $("#input-count").val();
        eel.search(searchText, count)
    });
});
