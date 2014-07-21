var map = L.mapbox.map('map', 'mzarafonetis.idm8dak7')
    .setView([40,-40.50],4)
    .addControl(L.mapbox.geocoderControl('mzarafonetis.idm8dak7'));

d3.csv("place_coordinates.csv", function(error, data) {
    d3.json("try_this2.json", function(error2, travels) {
	console.log("errors: ", error2)
	console.log("Travels: ", travels)
	for (var i=0; i<data.length; i++) {
	    var latlng = [parseFloat(data[i].latitude),parseFloat(data[i].longitude)]
	    var geojsonMarkerOptions = {
		radius:7,
		fillColor: "#fff",
		color: "#000",
		weight: 1,
		opacity: 1,
		fillOpacity: 0.8,
		title: data[i].place
	    };
	    
	    var circle = L.circleMarker(latlng,geojsonMarkerOptions).bindPopup(
		"<h2>"+data[i].place+"</h2>");
	    
	    circle.addTo(map);
	}
	/*
	This is used to show all of the lines, which is not necessarily what
	is needed right now. Need to make the decision for later on

	for (var j=0; j<travels.length; j++) {
	    var trips = travels[j]["Trips"];
	    for (var k=0; k<trips.length; k++) {
		var start = [39.9500,-75.1667];
		var end = findLocation(trips[k]["Place"]);
		if (end) {
		    var latlngs = [start,end];
		    var line = L.polyline(latlngs, {color: 'green', weight:3}).addTo(map);
		}
	    }
	}
	*/
	function findLocation(place) {
	    place = place.split(/(?=[A-Z])/);
	    for (var i=0; i<data.length; i++) {
		if (data[i].place.indexOf(place[0]) > -1) {
		    return [parseFloat(data[i].latitude),parseFloat(data[i].longitude)];
		}
	    }
	    console.log("Didn't find a match")
	}

	//////////// Now adding in the people //////////////
	for (var i=0; i<travels.length; i++) {
	    $("#people").append("<div id=\"person_"+travels[i].id+"\" class=person>"+travels[i].Person+"</div>");
	}

	///////////// Filtering people ////////////////////

	var colorPeople = d3.scale.category20();

	$(document).ready(function() {
	    $(".person").click(function() {
		$(this).toggleClass("selected");
		var id = $(this).attr("id");
		id = id.split("_")[1];
		var color = colorPeople(id);
		if ($(this).hasClass("selected")) {
		    $(this).css("background-color",color);
		    showLines(id, color);
		}
		else {
		    $(this).css("background-color","white");
		    hideLines(id, color);
		}
	    });
	});

	function showLines(id, c) {
	    for (var i=0; i<travels.length; i++) {
		if (travels[i]["id"] == id) {
		    for (var j=0; j< travels[i]["Trips"].length; j++) {
			var start = [39.9500,-75.1667];
			var end = findLocation(travels[i]["Trips"][j]["Place"]);
			if (end) {
			    var latlngs = [start,end];
			    var line = L.polyline(latlngs, {color: c, weight:3}).addTo(map);
			}
		    }
		    return null;
		}    

	    }
	}

	function hideLines(id, color) {
	    var lines = $("path");
	    for (var i=0; i<lines.length; i++) {
		console.log(lines[i]);
		console.log(lines[i].css("stroke"))
		if (lines[i].attr("stroke") == color) {
		    map.removeChild(lines[i]);
		}
	    }
	}
    });
});
