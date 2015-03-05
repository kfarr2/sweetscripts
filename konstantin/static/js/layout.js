$(document).ready(function(e){
    $('.arrows').css("visibility", "hidden");
    $('.latest').css("marginLeft", widest + 100);
    $('.latest').css("marginTop", -100);
    $('.arrows').css("color", "#ddd");
    $('.arrows').css("position", "fixed");
    $('.arrows.pull-right').css("marginLeft", widest - 60);
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
