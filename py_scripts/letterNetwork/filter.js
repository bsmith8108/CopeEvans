$(document).ready(function() {
    var is_up = [true,true];
    var slideHeight = 150;
    
    $("#timeline").css({"display":"none","height":slideHeight});
    $("#filter").css({"display":"none","height":slideHeight});


    $("#timeline-button").click(function() {
	if (is_up[0]) {
	    $("#timeline").css("display","block");
	    $("#footer-wrapper").css("bottom", slideHeight+15);
	    $("#footer").css("height",slideHeight);
	    $("#footer-transparent").css("bottom", slideHeight);
	    is_up[0] = false;
	}
	else {
	    $("#timeline").css("display","none");
	    $("#footer-wrapper").css("bottom",10);
	    $("#footer").css("height",60);
	    $("#footer-transparent").css("bottom", 0);
	    is_up[0] = true;
	}
    });

    $("#filters-button").click(function() {
	if (is_up[1]) {
	    $("#filter").css("display","block")
	    $("#footer").css("height",slideHeight);
	    $("#footer-wrapper").css("bottom",slideHeight+15);
	    $("#footer-transparent").css("bottom",slideHeight);
	    is_up[1] = false;
	}
	else {
	    $("#filter").css("display","none")
	    $("#footer").css("height",60);
	    $("#footer-wrapper").css("bottom",10);
	    $("#footer-transparent").css("bottom",0);
	    is_up[1] = true;
	}
    });
});
