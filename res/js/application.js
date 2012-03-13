$(document).ready(function(){

	$('.sitenav').tooltip({
      selector: "a[rel=tooltip]",
      placement: "bottom",
      animation: true
    })

});

$(window).load(function(){
        $('#slider').nivoSlider({
          effect:'fade',
          pauseTime: 5000,
          animSpeed: 500,
          keyboardNav: true,
        });
});