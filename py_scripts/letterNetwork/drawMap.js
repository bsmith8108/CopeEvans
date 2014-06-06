var map = L.mapbox.map('map', 'mzarafonetis.idm8dak7')
    .setView([40,-40.50],4)
    .addControl(L.mapbox.geocoderControl('mzarafonetis.idm8dak7'));

var line_info_list = [];
var line_info_dict = {};

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
	
	info_list = [];
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
	    line_info_dict[line._leaflet_id] = j;
	    line_info_list[j] = info;
	    
	    line.on('click', function(e) {
		openFancyBox(e.target._leaflet_id);
	    });
	}
	
	var all_paths = $("path");
	for (var k=0;k<all_paths.length; k++) {
	    $(all_paths[k]).attr("id","letter"+toString(k));
	}

	function openFancyBox(id) {
	    $.fancybox.open(info_list[id]);
	}

	$(".filter-button").click(function(d) {
	    var name = d.currentTarget.id;
	    $("#options").empty();
	    showFilterOptions(name);
	});

	var filterDict = {"age":[],"gender":[],"family":[],"transcript":[],"subject":[]};
	
	function showFilterOptions(name){
	    console.log(name);
	    var filterNames = {"age":"Age","gender":"Gender","family":"Creator","transcript":"Transcript","subject":"Subject"};
	    var optionsBox = $("#options");
	    var filterOptions = {"age":["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100"],
				 "gender":["M","F"],
				 "family":["Cope","Evans","Drinker","Stokes","Tyson","Other"],
				 "transcript":["Has Transcript","No Transcript"],
				 "subject":["travel","education","love","health","family","politics","lifestyle"]
				}
	    var myName = filterNames[name];
	    var myFilterOptions = filterOptions[name];
	    var counter = 0;
	    optionsBox.append("<div class=\"col\"><h2>Options:</h2></div>");
	    for (var i=0; i<myFilterOptions.length; i++) {
		if (i%3 == 0) {
		    optionsBox.append("<div class=\"col\" id=\"optionCol"+counter.toString()+"\">");
		    currentBox = $("#optionCol"+counter.toString());
		    counter++;
		}
		currentBox.append("<div class=\"options-button\" id=\""+myFilterOptions[i]+"\">"+myFilterOptions[i]+"</div>")
		var newItem = $("#"+myFilterOptions[i]);
		if (filterDict[name].indexOf(myFilterOptions[i]) > -1) {
		    newItem.css("background-color","yellow");
		}
		if (i%3 == 2) {
		    optionsBox.append("</div>");
		}
	    }
	    

	    $(".options-button").click(function(d) {
		var option = d.currentTarget.id;
		if ($(this).css("background-color") == "rgb(70, 130, 180)") {
		    $(this).css("background-color","yellow");
		    updateDict(name,option);
		    filterMap();
		}
		else {
		    $(this).css("background-color","steelblue");
		    updateDict(name,option);
		    filterMap();
		}
	    });
	}

	function updateDict(name,option) {
	    if (filterDict[name].indexOf(option) > -1) {
		var exclude = filterDict[name].indexOf(option);
		var newList = [];
		for (var i=0; i<filterDict[name].length; i++) {
		    if (i == exclude) {
			continue;
		    }
		    else {
			newList.push(filterDict[name][i]);
		    }
		}
		filterDict[name] = newList;
	    }
	    else {
		filterDict[name].push(option);
	   }
	}
    
	function filterMap() {
	    var filterNames = {"age":"Age of Author","gender":"Gender of Author","family":"Family","transcript":"Transcript","subject":"Subject"};
	    var keys = ["age","gender","family","transcript","subject"];
	    var lines= $("path");
	    var keys_used = [];
	    for (var i=0; i<keys.length; i++) {
		if(filterDict[keys[i]].length > 0) {
		    keys_used.push(keys[i]);;
		}
	    }  

	    for (var j=0; j<lines.length; j++) {
		var shouldAdd = true;
		var line_json =line_info_list[j];
		var family = findFamily(line_json["Creator"])
		line_json["Family"] = family;
		for (var k=0; k<keys_used.length;k++) {
		    var keyAllGood = false;
		    var myKey = keys_used[k];
		    if (!(myKey == "transcript")) {
			for (var m=0; m<filterDict[myKey].length; m++) {
			    if (line_json[filterNames[myKey]] == filterDict[myKey][m]) {
				keyAllGood = true;
			    }
			}
		    }
		    else {
			if(line_json["Transcript"].split(" ").length < 2 && filterDict[myKey].indexOf("No Transcript") > -1) {
			    keyAllGood = true;
			}
			else if(line_json["Transcript"].split(" ").length >= 2 && filterDict[myKey].indexOf("Has Transcript") > -1) {
			    keyAllGood = true;
			}
			else {
			    keyAllGood = false;
			}
		    }
		    if (!keyAllGood) {
		        shouldAdd = false;
		    }
		}

		if(shouldAdd) {
		    $(lines[j]).css("visibility","visible");
		}
		else {
		    $(lines[j]).css("visibility","hidden");
		}
	    }
	}
	
	function findFamily(name) {
	    var split_name = name.split(/(?=[A-Z])/);
	    for (var i=0;i<split_name.length;i++) {
		split_name[i] = split_name[i].replace(/[^a-zA-z]/g,"");
	    }

	    var family_names = ["Cope","Evans","Drinker","Stokes","Tyson"];
	    for (var i=split_name.length-1; i>=0; i--) {
		if (family_names.indexOf(split_name[i]) > -1) {
		    return split_name[i];
		}
	    }

	    return "Other";
	}
    });
});

