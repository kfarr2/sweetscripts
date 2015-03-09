$(document).ready(function(e){
    $('.latest').css("marginLeft", widest + 100);
    $('.latest').css("marginTop", -100);
    $(setTimeout(
        function(){
            $('.welcome').animate({ "margin-left": -widest-500 }, 1000, "swing");
            $('.latest').animate({ "margin-left":  0}, 900);
        }, 1500)
    );
});
