function mapInit() {
	var mapCenter = new google.maps.LatLng(53.3498,-6.2603);
	var mapCanvas = document.getElementById("googleMap");
	var mapOptions = {center: mapCenter, zoom: 14};
	var map = new google.maps.Map(mapCanvas, mapOptions);
		
	var locations = [
     	['O\'Connell St./Princes St.', 53.35, -6.26, 33],
      	['Cathal Brugha Street', 53.351498594, -6.25499898, 24],
      	['Parnell St.', 53.35186, -6.26285, 31],
      	['Custom House', 53.34818, -6.25045, 23],
      	['Jervis St.', 53.34692, -6.26596]
	];
		
	for(i = 0; i <locations.length; i++) {
		var position = new google.maps.LatLng(locations[i][1], locations[i][2]);
        marker = new google.maps.Marker({
            position: position,
            map: map
        });
     }
}