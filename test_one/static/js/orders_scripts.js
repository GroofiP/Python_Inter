window.onload = function () {
    $('.basket_list').on('click',".yo", function () {
        $.ajax({
            url: "/save_form/",

            success: function (data) {
                console.log(data)
                $('.js-create-good').html(data);
            }
        });
    })
    return;
};
