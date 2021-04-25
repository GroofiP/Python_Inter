$(document).ready(function() {
    $("#modal-good").submit(function(){
        let form = $(this);
        $.ajax({
            url: "/save-form/",
            type: "post",
            dataType: 'json',
            contentType: false, // важно - убираем форматирование данных по умолчанию
            processData: false,
            success: function(data) {
                if (data.form_is_valid) {
                    $("#good-table body").html(data.html_good_list);
                    $("#modal-good").modal("hide");
                }
                else {
                    $("#modal-good .modal-content").html(data.html_form);
                }},
            error: function(error) {
                console.log(error)
                }
        });
        return false;
    });
});
