function mapInit() {
	var mapCenter = new google.maps.LatLng(53.3498,-6.2603);
	var mapCanvas = document.getElementById("googleMap");
	var mapOptions = {center: mapCenter, zoom: 14};
	var map = new google.maps.Map(mapCanvas, mapOptions);
	
  	var xhttp = new XMLHttpRequest();
  	xhttp.onreadystatechange = function() {
    	if (this.readyState == 4 && this.status == 200) {
      		locations = JSON.parse(this.responseText);
      			
      	// Create empty array 'index'
	var index = [];
	// Add (i.e. 'push') the next xID item to the array
      	for(var xID in locations) {
      		index.push(xID);		
      		}
      			
      	// Fill map up with markers based on json data
	for(i = 0; i < index.length; i++) {
      			
	var position = new google.maps.LatLng(locations[index[i]].latitude, locations[index[i]].longitude);
        marker = new google.maps.Marker({position: position, map: map});}
		
	}};
  	xhttp.open("GET", "static/stations.json", true);
  	xhttp.send();
}
