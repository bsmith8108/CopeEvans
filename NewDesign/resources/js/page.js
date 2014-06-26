$(document).ready(function() {
    $("div.info").css("display","none");
    $(".content:first-child").children("div").slideDown();
    $(".content:first-child").children("div").addClass("selected");
    $(".content h2").click(function() {
	$(this).next().toggleClass("selected")
	console.log($(this).next())
	if (!$(this).next().hasClass("selected")) {
	    $(this).next().slideUp();
	}
	else {
	    $(this).next().slideDown();
	}
    });
});
