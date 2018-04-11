function mapInit() {
	var mapCenter = {lat: 53.3498, lng: -6.2603};
    var map = new google.maps.Map(document.getElementById('googleMap'), {
    zoom: 14, 
    center: mapCenter});
    
    //var markerArray = [];
    //var markerCounter = 0;
  		
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
             
			var position = new google.maps.LatLng(data[index[i]].latitude, data[index[i]].longitude);
        	var contentString = '<div class="infoWindowOpen">' +
        						'<h2>' + index[i] + '</h2>' +
        						'<p>Available Bikes: ' + data[index[i]].available_bikes + '</p>' +
        						'<p>Available Bike Stands: ' + data[index[i]].available_stands + '</p>' +
        						'</div>';
        			
        	var myinfowindow = new google.maps.InfoWindow({content: contentString});
        			
    		var marker = new google.maps.Marker({
    			position: position, 
    			map: map,
    			infowindow: myinfowindow
    			//markerID: markerCounter
    		});
    		
    		//markerArray.push(marker);
    				
    		google.maps.event.addListener(marker, 'click', function() {
        		
        		//var x = markerArray[markerCounter].get("markerID");
        		//markerArray[0]['infowindow'].open(map, this);
        		//alert(x);
        		//console.log(markerArray);
        		
        		this.infowindow.open(map, this);
        		
			});
			
			//markerCounter++;
    				
		}
				
	});

}
      	
window.setInterval(function(){
  	mapInit()
}, 300000);