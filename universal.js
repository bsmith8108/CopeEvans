function getData(file) {
    var file_extension = file + ".txt";
    $("#people_info").empty();
    $("#people_info").load(file_extension);
}
