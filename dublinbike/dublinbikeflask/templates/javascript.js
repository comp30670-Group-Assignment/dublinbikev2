// This code initializes a map on the page where it is called
      function initMap() {
          // Tell the map where to start from...
        var myLatLng = {lat: 53.3498, lng: -6.2603};
          
        /*var station_1 = {lat: 53.35, lng: ;
        var station_2 = {lat: , lng: };*/
          
        var infowindow = new google.maps.InfoWindow();

        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 16,
          center: new google.maps.LatLng(53.3498, -6.2603)
        });

        /*var marker = new google.maps.Marker({
          position: station_1,
          map: map,
          title: 'O\'Connell St.'
        });
          
        var marker = new google.maps.Marker({
          position: station_2,
          map: map,
          title: 'Drumcondra'
        });*/
          
        var locations = [
     		['O\'Connell St./Princes St.', 53.35, -6.26, 33],
      		['Cathal Brugha Street', 53.351498594, -6.25499898, 24],
      		['Parnell St.', 53.35186, -6.26285, 31],
      		['Custom House', 53.34818, -6.25045, 23],
      		['Jervis St.', 53.34692, -6.26596]
    	];
          
          
        var marker, i;
          for (i = 0; i < locations.length; i++) {  
              marker = new google.maps.Marker({
                  position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                  map: map
      });
        
          google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]+"<br>"+"Station no.: "+locations[i][3]+"<br>"+"Bikes available: "+locations[i][4]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
              
       
          // How do I get it to add multiple markers all at once, reading from a JSON file?
          
      }
