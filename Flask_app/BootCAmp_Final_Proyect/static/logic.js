// Add console.log to check to see if our code is working.
console.log("working");
console.log(API_KEY);
// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// We create the second tile layer that will be the background of our map.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

let dark = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/dark-v10/tiles/{z}/{x}/{y}?access_token={accessToken}', {
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
	maxZoom: 18,
	accessToken: API_KEY
});

// Make México the center of the map 
// Create the map object with center, zoom level and default layer.
let map = L.map('mapid', {
	center: [15.456255132489616, -40.52737566136505],
	zoom: 3,
	layers: [dark]
});

// Create a base layer that holds all three maps.
let baseMaps = {
  "Streets": streets,
  "Satellite": satelliteStreets,
  "Dark": dark
};

// Then we add a control to the map that will allow the user to change which
// layers are visible.
L.control.layers(baseMaps).addTo(map);

// Accessing the airport GeoJSON URL
let cityData2 = "../static/resources/cities2.json"           //"static/resources/cities2.json"

//Grabbing our GeoJSON data.
d3.json(cityData2).then(function(data) {
    console.log(data);



    // Fuction for the style of the circle 
    function styleInfo(feature) {
        return {
            opacity: .5,
            fillOpacity: .5,
            radius: getSize(feature.properties.Retweet_Count),
            // radius: (feature.properties.Retweet_Count),
            fillColor: getColor(feature.properties.Sentiment),
            color: "white",
            stroke: true,
            weight: 0.5
        };
    }

   //let retweet_porperty = feature.properties.Retweet_Count

    function getSize(retweet) {
        if (retweet < 200) {
            return 10;
        }

        

        return retweet/30
    }  


    function getColor(sentiment_analysis) {
        if(sentiment_analysis == "Negative") {
            return "#092a5c";
        }
            return "#00ffcd"
    }


    L.geoJson(data, {
        pointToLayer: function(feature, coordinates) {
            console.log(data);
            return L.circleMarker(coordinates);
        },
            style: styleInfo,

                onEachFeature: function(feature, layer) {
                    layer.bindPopup("<h3>City: " + feature.properties.City +  
                    "</h3> <hr> <h4>Sentiment: " + feature.properties.Sentiment + 
                    "</h4> <h4> Retweet Count: " + feature.properties.Retweet_Count +
                    "</h4> <h4> Verified Account: " + feature.properties.Verified_Account +
                    "</h4> <h4> Country: " + feature.properties.Country +
                    "</h4>");
                }
                    
        }).addTo(map);

    // Here we create a legend control object.
    let legend = L.control({
        position: "topcenter"
    });

    // // Then add all the details for the legend
    // legend.onAdd = function() {
    // let div = L.DomUtil.create("div", "info legend");

    // const sentiment = [0, 1];
    // const sentiment_colors = [
    //     "#98ee00",
    //     "#d4ee00",
    
    // ];
      
    //   // Looping through our intervals to generate a label with a colored square for each interval.
    //     for (var i = 0; i < magnitudes.length; i++) {
    //       console.log(colors[i]);
    //       div.innerHTML +=
    //         "<i style='background: " + colors[i] + "'></i> " +
    //         magnitudes[i] + (magnitudes[i + 1] ? "&ndash;" + magnitudes[i + 1] + "<br>" : "+");
    //       }
    //       return div;
    //     };
    
     // Finally, we our legend to the map.
        //legend.addTo(map);

});




// // WHAT IS WORKING
// // Grabbing our GeoJSON data.
// d3.json(cityData2).then(function(data) {
//     console.log(data);
//     L.geoJson(data, {
//         pointToLayeer: function(features,latlng) {
//             console.log(data);
//             return L.circleMarker(latlng);},
//                 // color: 'red',
//                 // fillColor: '#f03',
//                 // fillOpacity: 0.5,
//                 // radius: 500
            
        
//     }).addTo(map);
// });

// // map.addTo(map);







