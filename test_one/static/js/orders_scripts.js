window.onload = function () {
    $('.js-create-good').on('click', function () {
        let btn = $(this);
        $.ajax({
            url: "/save_form/",
            type: 'get',
            dataType: 'json',
            contentType: false, // важно - убираем форматирование данных по умолчанию
            processData: false,
            beforeSend: function(data) {
                $("#modal-good").modal("show");
            },
            success: function(data) {
                $("#modal-good .modal-content").html(data.html_form);
            },

        });
    })
};
