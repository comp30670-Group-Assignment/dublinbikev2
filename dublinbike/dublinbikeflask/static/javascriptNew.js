// Hold marker data.
var markerArray = [];
var map;

function mapInit() {
	var mapCenter = {lat: 53.3498, lng: -6.2603};
    map = new google.maps.Map(document.getElementById('googleMap'), {
    zoom: 14, 
    center: mapCenter});
    
    // Count number of markers initiated.
    var markerCounter = 0;
    // Hold modal data.
    var modalArray = [];
  		
  	$.getJSON($SCRIPT_ROOT + '/_map_data', function(data) {
      				
      	// Create empty array 'index'
		var index = [];
		// Add (i.e. 'push') the next xID item to the array
      	for(var xID in data) {
      		index.push(xID);		
      	}
      			
      	// Fill map up with markers based on json data
        // Right now all markers are being generated, but they are being given all the same
        // content, when they should be given content depending on their own personal info.
		for(i = 0; i < index.length; i++) {
    		var mytext = index[i] + "<br> Station No.: " + "<br> Free bikes: ";
    		var myinfowindow = new google.maps.InfoWindow({content: mytext});
            // We've looped through to the end of the loop, so now i has the final value...
            var e = index[i];
            
            
    
    		// Push to array to store data returned by $.getJSON.
    		modalArray.push(data[index[i]]);
    		
    		var iconBase = '/static/';
			// Red
			if (data[index[i]].available_bikes < 5){
				var iconVal = iconBase + 'red.png';
    		// Green
    		} else if (data[index[i]].available_bikes > 30){
				var iconVal = iconBase + 'green.png';
    		//Amber
    		} else {
    			var iconVal = iconBase + 'amber.png';
    		}
             
			var position = new google.maps.LatLng(data[index[i]].latitude, data[index[i]].longitude);
        	var contentString = '<div class="infoWindowOpen">' +
        						'<h4 id="info-head">' + index[i] + '</h4>' +
        						'<p class="info-text">Available Bikes: ' + data[index[i]].available_bikes + '</p>' +
        						'<p class="info-text">Available Bike Stands: ' + data[index[i]].available_stands + '</p>' +
        						'<button type="button" class="btn map-button" id="mapBtn">Open Data</button>' +
        						'</div>';
        
            
        	var myinfowindow = new google.maps.InfoWindow({content: contentString});
           
    		var marker = new google.maps.Marker({
    			position: position, 
    			map: map,
    			infowindow: myinfowindow,
    			markerID: markerCounter,
    			icon: iconVal
    		})	
            
            ;
            
            
    		
    		markerArray.push(marker);
    		open = [];
    		google.maps.event.addListener(marker, 'click', function() {
    			var x = this.markerID;
        		if (open.length != 0) {
        			for(var i = 0; i < open.length;i++) {

        				markerArray[open[i]]['infowindow'].close();
        			}
        		}
        		markerArray[x]['infowindow'].open(map, this);
        		
        		open.push(x)
        		
        		// Map modal.
				$(document).ready(function(){
    				$("#mapBtn").click(function(){
        				$("#mapModal").modal();
        				$("#modal-map-head").html("<h2 id='modal-title' style='text-align:center;font-weight:bold'>"+index[x]+"</h2>");
    				});
				});
				
// Load google charts
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);
google.charts.setOnLoadCallback(drawVisualization2);
                
// Draw the chart and set the chart values
function drawVisualization() {
var bensonSt = [2000, 2000, 1000];
var blackhallPlace = [1500, 1500, 1500];
    
var data = google.visualization.arrayToDataTable([
['day', 'Humidity', 'Temperature', 'Occupancy'],
['09:00',  bensonSt[0],      bensonSt[1],      bensonSt[2]],
['12:00',  100,      1120,        599],
['15:00',  165,      938,      614.6],
['18:00',  165,      938,      614.6],
['21:00',  165,      938,      614.6],
['00:00',  165,      938,      614.6]
]);

//var e = index[0];

var options = {
title : e,//'Predicted Station Occupancy Based on Humidity and Temperature',
vAxis: {title: 'units'},
hAxis: {title: 'time'},
'width':650,
'height':400,
series: {2: {type: 'line'}}
};

var chart = new google.visualization.ComboChart(document.getElementById('modal-graph'));
chart.draw(data, options);
}
                
                
function drawVisualization2() {
 
var bensonSt = [2000, 2000, 1000];
var blackhallPlace = [1500, 1500, 1500];
var data = google.visualization.arrayToDataTable([
['day', 'Humidity', 'Temperature', 'Occupancy'],
['Mond',  bensonSt[0],      bensonSt[1],      bensonSt[2]],
['Tues',  100,      1120,        599],
['Wed',  165,      938,      614.6],
['Thurs',  165,      938,      614.6],
['Fri',  165,      938,      614.6],
['Sat',  165,      938,      614.6],
['Sun',  165,      938,      614.6]
]);
    
var options = {
'width':650,
'height':400,
title : 'Station Occupancy Trend This Past Week',
vAxis: {title: 'units'},
hAxis: {title: 'Day'},
seriesType: 'bars',
};

var chart = new google.visualization.ComboChart(document.getElementById('weather-trend'));
chart.draw(data, options);
}
			});
			
			markerCounter++;
    				
		}
				
	});

}
      	
window.setInterval(function(){
  	mapInit()
}, 300000);

// Trigger Google Maps marker infowindow.
function markerFlag(markerNum) {
	google.maps.event.trigger(markerArray[markerNum], 'click');
}

// Get station marker names and populate dropdown menu.
$.getJSON($SCRIPT_ROOT + '/_drop_data', function(data) {

	// Append marker locations to dropdown menu.
	for (var i = 0; i < data.length; i++) {
		$("#marker-loc").append("<a href='#' onclick='markerFlag("+i+")'>"+data[i]+"</a>");
	}

});
