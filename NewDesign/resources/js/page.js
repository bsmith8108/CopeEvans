$(document).ready(function() {
    $("p.info").slideUp();
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
