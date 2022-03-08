var diameter = 400

var color = d3.scaleOrdinal()
    .range(["#75bde0", "#97dbae", "#cde4ad"])

var pack = d3.pack()
  .size([diameter, diameter])
  .padding(2)

var vis = d3.select("#svgid").append("svg")
  .attr("width", diameter)
  .attr("height", diameter)
  .attr("class", "pack")
  .append("g");

//DRAW CHART

d3.csv("tweets.csv", function(data) {

  var root = { name: "sentiment", children: data };
    
//UPDATE DATA

    tweets = d3.hierarchy(root)
      .sum(function(d) { return d.tweets })

    function rank(data) {    
    
    pack(data);

    var node = vis.selectAll("circle")
      .data(data.descendants())
      .enter()
      .append("circle")
        .attr("class", "node")
        .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
        .attr("r", function(d) { return d.r; })
        .attr("fill", function(d) {
            return color(d.data.sentiment);
        
      })
   
    node.append("text")
        .text(function (d) {return d.name; });

    node.exit().remove();

  }
 
  rank(tweets);

  
  
})
