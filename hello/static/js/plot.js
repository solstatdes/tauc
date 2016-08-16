function plot (data, target) {
    console.log(data)
       
    $('#'+target).empty();
    w = $('#'+target).width();
    h = (0.75*w);
    var padding = 40;

    d3.select('#'+target).selectAll("svg").remove();

    var svg = d3.select("#"+target)
                .append("svg:svg")
                .attr("width", w)
                .attr("height", h);

    var xScale = d3.scale.linear()
                   .domain([d3.min(data, function(d) { return d[0]; }), d3.max(data, function(d) { return d[0]; })])
                   .range([padding, w-padding]);

    var yScale = d3.scale.linear()
                   .domain([d3.min(data, function(d) { return d[1]; }), d3.max(data, function(d) { return d[1]; })])
                   .range([h-padding, padding]);

    var xAxis = d3.svg.axis()
                      .scale(xScale)
                      .orient("bottom");

    var yAxis = d3.svg.axis()
                      .scale(yScale)
                      .orient("left");

    svg.selectAll("circle")
       .data(data)
       .enter()
       .append("circle")
       .attr("cx", function(d) {
           return xScale(d[0]);
       })
       .attr("cy", function(d) {
           return yScale(d[1]);
       })
       .attr("r", 8)
       .style("fill", "blue");

    svg.append("g")
       .attr("class", "axis")
       .attr("transform", "translate(0," + (h-padding) + ")")
       .call(xAxis)

   svg.append("g")
      .attr("class", "axis")
      .attr("transform", "translate(" + padding + ",0)")
      .call(yAxis);

    



    
}

