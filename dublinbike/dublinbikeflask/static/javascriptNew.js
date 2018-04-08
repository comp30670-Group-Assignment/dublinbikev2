// Alasa's function to open up a new pop-up window when one of the markers is selected.
// The URL needs to be changed to show the weather and station Google charts, etc.
function poponclick(){
    var testwindow = window.open("http://www.this-page-intentionally-left-blank.org/", "_blank",  "width=600,height=400");
    testwindow.moveTo(400, 400);
}
  
function mapInit() {    
	var mapCenter = {lat: 53.3498, lng: -6.2603};
    var map = new google.maps.Map(document.getElementById('googleMap'), {
        zoom: 14, 
        center: mapCenter});
    
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
        	// Right now all markers are being generated, but they are being given all the same
        	// content, when they should be given content depending on their own personal info.
			for(i = 0; i < index.length; i++) {
                var myUrl = "stations/"+i;
    			
                var mytext = index[i] + "<br> Station No.: " + "<br> Free bikes: <br>" + "<a id='popUp' href='#' onclick='poponclick();return false;'>Click for more details</a>";
                
               
                
    			var myinfowindow = new google.maps.InfoWindow({content: mytext});
             
				var position = new google.maps.LatLng(locations[index[i]].latitude, locations[index[i]].longitude);
        
    			var marker = new google.maps.Marker({
    				position: position, 
    				map: map,
    				infowindow: myinfowindow
    			});
        
    		google.maps.event.addListener(marker, 'click', function() {
        		this.infowindow.open(map, this);

			});
		
		}      
            
	}};
  	xhttp.open("GET", "static/stations.json", true);
  	xhttp.send();
}
