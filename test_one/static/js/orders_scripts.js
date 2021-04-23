window.onload = function () {
    $('.yo').on('click', function () {
        $.ajax({
            url: "/save_form/",

            success: function (data) {
                console.log(data)
                $('.js-create-good').html(data);
            }
        });
    })
    $('.js-good-create-form').submit(function(e) {
        e.preventDefault();
        let $form = $(this);
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),

        }).done(function(data) {
            $('body').html(data);
        }).fail(function() {
            console.log('fail');
        });
        //отмена действия по умолчанию для кнопки submit
        e.preventDefault();
    });
    return;
};
