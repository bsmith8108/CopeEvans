$(document).ready(function() {
    var isUp = false;
    $("#explore").click(function() {
	if (!isUp){
	    $("#menu:hidden").css("display","block");
	    $("#menu").animate( {
		height:'400px',
		opacity:"1",
		display:"block"
	    });
	    $(this).animate({
	    bottom: '+=400px'
	    });
	    isUp = true;
	}
	else {
	    $("#menu").animate( {
		height:'0px',
		opacity:"0",
	    });
	    $(this).animate({
	    bottom: '-=400px'
	    },
	    { duration: 1000 });
	    $("#menu").css("display","none");
	    isUp = false;
	}   
    });
});
