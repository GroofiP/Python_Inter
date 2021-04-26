$(document).ready(function() {
    $('.js-good-create-form').submit(function(e) {
        e.preventDefault();
        let $form = $(this);
        $.ajax({
            type: $form.attr('method'),
            url: $form.attr('action'),
            data: $form.serialize(),

        }).done(function(data) {
            $('.basket_list').html(data);
        }).fail(function() {
            console.log('fail');
        });
        //отмена действия по умолчанию для кнопки submit
        e.preventDefault();
    });
});
