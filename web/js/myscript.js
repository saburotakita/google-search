$(function(){
    $btn = $("#btn-search").click(() => {
        const searchText = $("#input-search-text").val();
        const count = $("#input-count").val();
        eel.search(searchText, count)
    });
});
