$(document).ready(function() {
    var isUp = false;
    $("#explore").click(function() {
	if (!isUp){
	    $("#menu").css("bottom","0px");
	    $("#menu").animate( {
		height:'400px',
		opacity:"1"
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
		bottom:"30px"
	    });
	    $(this).animate({
	    bottom: '-=400px'
	    });
	    isUp = false;
	    $("#menu").css("bottom","30px");
	}   
    });
});
