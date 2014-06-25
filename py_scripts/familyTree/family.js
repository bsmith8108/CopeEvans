
var width = 1300,
    height = 900;

var cluster = d3.layout.cluster()
    .size([height, width - 160]);

var diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(40,0)");

d3.json("familytree.json", function(error, root) {
  var nodes = cluster.nodes(root),
      links = cluster.links(nodes);
  
  console.log(nodes)
  console.log(links)
  var link = svg.selectAll(".link")
      .data(links)
    .enter().append("path")
      .attr("class", "link")
      .attr("d", diagonal)
      .attr("id", function(d) { return d.source["Partner"] + d.target["Partner"]; });

  var node = svg.selectAll(".node")
      .data(nodes)
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })

  node.append("circle")
      .attr("r", 4.5)
      .on("click", function(d) {
	    var text = "<div class=\"close\">-</div>"
	    text = text + "<b>Partner:</b> " + d.Partner + "<br>";
	    text = text + "<b>Children:</b> <br>";
	    if (d.children != undefined) {
		for (var i=0; i<d.children.length; i++) {
		    text = text + "<div class=\"child\">"+ d.children[i]["Cope Member"] + " and "+d.children[i]["Partner"]+"</div>";
		}
	    }
	    console.log($(this)[0].getAttribute("class"))
	    if ($(this)[0].getAttribute("class") != "selected") {
		highlightChildren(d);
		console.log($(this)[0].getAttribute("class"))
	    }
	    else {
		console.log("here");
		$(this)[0].removeClass("selected");
	    }
	    $("#info").html(text);
      });

  node.append("text")
      .attr("dx", function(d) { return d.Children ? -8 : 8; })
      .attr("dy", 3)
      .style("text-anchor", function(d) { return d.Children ? "end" : "start"; })
      .text(function(d) { return d["Cope Member"]; });
});

function highlightChildren(data) {
    var lines = $(".link");
    for (var i=0; i<lines.length; i++) {
	var id = lines[i].getAttribute("id");
	for (var j=0; j<data.children.length; j++) {
	    var child = data.children[j].Partner;
	    if (id.indexOf(data["Partner"]) > -1 && id.indexOf(child)) {
		lines[i].style.stroke = "yellow";
	    }
	}
    }
}

d3.select(self.frameElement).style("height", height + "px");

$(".close").live("click", function() {
    $("#info").toggleClass("hidden");
    if ($("#info").hasClass("hidden")) {
	$(".close").text("+");
    }
    else {
	$(".close").text("-");
    }
});
