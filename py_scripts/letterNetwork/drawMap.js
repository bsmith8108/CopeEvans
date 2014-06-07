var map = L.mapbox.map('map', 'mzarafonetis.idm8dak7')
    .setView([40,-40.50],4)
    .addControl(L.mapbox.geocoderControl('mzarafonetis.idm8dak7'));

var line_info_list = [];
var line_info_dict = {};
var filterDict = {"age":[],"gender":[],"family":[],"transcript":[],"subject":[], "author":[]};

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
	
	var all_paths = $("path.leaflet-clickable");
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

	
	function showFilterOptions(name){
	    var filterNames = {"age":"Age","gender":"Gender","family":"Creator","transcript":"Transcript","subject":"Subject","author":"Author"};
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
	    if (name == "author") {
		optionsBox.append("<div class=\"col\" id=\"authorSelect\">");
		var current =$("#authorSelect");
		current.append("<a href=\"pageRank.html\" data-fancybox-type=\"iframe\" class=\"people-select\"><div class=\"options-button\" id=\"AboutPR\">About the Network</div></a>");
		current.append("<a href=\"index.html\" data-fancybox-type=\"iframe\" id=\"authorsFrame\" class=\"people-select\"><div class=\"options-button\" id=\"selectAuthor\">Select authors</div></a>");
		optionsBox.append("</div>");
	    }
	    else {
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
	    console.log("poop")
	    var filterNames = {"age":"Age of Author","gender":"Gender of Author","family":"Family","transcript":"Transcript","subject":"Subject"};
	    var keys = ["age","gender","family","transcript","subject"];
	    var lines= $("path.leaflet-clickable");
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
	/*################# CODE TO CREATE THE CATEGORICAL FILTERS ABOVE #####################
	Variables I need from above:
	    -line_info_list

	###################### CODE TO CREATE THE TIMELINE BELOW ###########################*/
	
	// The call to the makeTimeline function will be needed on load, just easier to separate
	// into its own function, in case it needs to me moved

	function makeTimeline() {
	    var margin = {top: 0, right: 40, bottom: 50, left: 40},
		width = 960 - margin.left - margin.right,
		height = 100 - margin.top - margin.bottom;

	    var x = d3.time.scale()
		.domain([new Date(1819, 11, 1), new Date(1920, 1, 1) - 1])
		.range([0, width]);

	    var brush = d3.svg.brush()
		.x(x)
		.extent([new Date(2013, 7, 2), new Date(2013, 7, 3)])
		.on("brush", brush)
		.on("brushstart",brushstarted);

	    var svg = d3.select("body").select("#footer").select("#timeline-inside").append("svg")
		.attr("width", width + margin.left + margin.right)
		.attr("height", height + margin.top + margin.bottom)
	      .append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	    svg.append("rect")
		.attr("class", "grid-background")
		.attr("width", width)
		.attr("height", height);

	    svg.append("g")
		.attr("class", "x grid")
		.attr("transform", "translate(0," + height + ")")
		.call(d3.svg.axis()
		    .scale(x)
		    .orient("bottom")
		    .ticks(d3.time.years, 10)
		    .tickSize(-height)
		    .tickFormat(""))
	      .selectAll(".tick")
		.classed("minor", function(d) { return d.getHours(); });

	    svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(d3.svg.axis()
		.scale(x)
		.orient("bottom")
		.ticks(d3.time.years,10)
		.tickPadding(0))
	      .selectAll("text")
		.attr("x", 6)
		.style("text-anchor", null);

	    var gBrush = svg.append("g")
		.attr("class", "brush")
		.call(brush)
		.call(brush.event);

	    gBrush.selectAll("rect")
		.attr("height", height);

	    function brush() {
		if (!d3.event.sourceEvent) return; // only transition after input
		var extent0 = brush.extent(),
		extent1 = extent0.map(d3.time.year.round);

		// if empty when rounded, use floor & ceil instead
		if (extent1[0] >= extent1[1]) {
		    extent1[0] = d3.time.year.floor(extent0[0]);
		    extent1[1] = d3.time.year.ceil(extent0[1]);
		}
	  
		var startYear = extent1[0].getFullYear();
		var endYear = extent1[1].getFullYear();
		var re = new RegExp("[0-9][0-9][0-9][0-9]")
		var lines = $("path.leaflet-clickable");
		
		for (var i=0;i<lines.length; i++) {
		    line_json = line_info_list[i];
		    var myYear = getYear(line_json["Date"]);
		    if (myYear > startYear && myYear < endYear) {
			$(lines[i]).css("visibility","visible");
		    }
		    else {
			$(lines[i]).css("visibility","hidden");
		    }
		}
	    }
	    
	    function getYear(date_string) {
		date_list = date_string.split("-");
		return date_list[0];
	    }
	    function brushstarted() {
		console.log("here");
	    }
	}

	makeTimeline();
    });
});

