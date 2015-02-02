$(document).ready(function(e){
    $('.latest').css("marginLeft", widest + 100);
    $('.latest').css("marginTop", -100);
    $('.arrows').css("z-index", -1);
    $('.arrows').css("color", "#ddd");
    $(setTimeout(
        function(){
            $('.welcome').animate({ "margin-left": -widest-500 }, 1000, "swing");
            $('.latest').animate({ "margin-left":  0}, 900);
        }, 1500)
    );
});

$(document).mousemove(function(e){
    var mouse = e.pageX;
    if (mouse < 100 || mouse > widest - 100){
        $('.arrows').css("visibility", "visible");
    } else {
        $('.arrows').css("visibility", "hidden");
    }
});
