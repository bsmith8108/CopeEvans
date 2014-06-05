var map = L.mapbox.map('map', 'mzarafonetis.idm8dak7')
    .setView([40,-40.50],4)
    .addControl(L.mapbox.geocoderControl('mzarafonetis.idm8dak7'));

d3.csv("partialCurrectLocations.csv", function(error, data) {
    d3.csv("letterTravels.csv", function(error, travel) {
	console.log("travel",travel)
	console.log("data",data)
	for (var i=0; i<data.length; i++) {
	    var temp = L.mapbox.featureLayer().addTo(map);

	    var geojson = {
	    type: 'FeatureCollection',
	    features: [{
		type: 'Feature',
		    properties: {
			title: data[i].Name,
			'marker-color':'#f86767',
			'marker-size':'small'
		    },
		    geometry: {
			type: 'Point',
			coordinates:[parseFloat(data[i].Longitude),parseFloat(data[i].Latitude)]
		    }
		}]
	    };

	    temp.setGeoJSON(geojson);
	    temp.on('mouseover', function(e) {
		e.layer.openPopup();
	    });
	    temp.on('mouseout', function(e) {
		e.layer.closePopup();
	    });
	}
	/*
	latlngs = [
	    [0,0],
	    [40,-74.50]
	  ];
	var line = L.polyline(latlngs, {color: 'red', weight:3}).addTo(map);
	*/
	info_list = [];
	var counter = 0;
	for (var j=0;j<travel.length;j++) {
	    var origin = [parseFloat(data[travel[j].Poo].Latitude),parseFloat(data[travel[j].Poo].Longitude)];
	    var destination = [parseFloat(data[travel[j].Dest].Latitude),parseFloat(data[travel[j].Dest].Longitude)];
	    var latlngs = [origin,destination];
	    var info = travel[j].Letter;
	    info = JSON.parse(info);
	    var t_Has = info.Transcript.split(" ").length;
	    if (t_Has > 2) {
		var line = L.polyline(latlngs, {color: 'green', weight:3}).addTo(map);
	    }
	    else {
		var line = L.polyline(latlngs, {color: 'red', weight:3}).addTo(map);
	    }
	    var info_string = "<h2>"+info.Title.split("COMMA").join(",")+"</h2>";
	    info_string = info_string + "Creator: " + info.Creator + "<br>";
	    info_string = info_string + "Recipient: " + info.Recipient;
	    info_string = info_string + "<br>Transcript: <br>" + info.Transcript.split("COMMA").join(",");
	    info_list[line._leaflet_id] = info_string;

	    line.on('click', function(e) {
		openFancyBox(e.target._leaflet_id);
	    });

	    counter++;
	}
	
	function openFancyBox(id) {
	    $.fancybox.open(info_list[id]);
	}
    });
});