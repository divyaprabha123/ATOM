// Eslint configuration for editor.
/* globals google */
/* eslint-env browser */
/* eslint quotes: ["warn", "single"]*/

function initMap() {
  const map = new google.maps.Map(document.querySelector('#map'), {
    zoom: 15,
    center: {
      // CIT Coimbatore
      lat: 11.0283,
      lng: 77.0273
    }
  });
  map.data.loadGeoJson('/data/subway-stations');
   var iconBase =
            'http://maps.google.com/mapfiles/kml/shapes/';

        var icons = {
          potholes: {
            icon: iconBase + 'mechanic.png'
          },
          road_sign: {
            icon: iconBase + 'forbidden.png'
          },
          road_furniture: {
            icon: iconBase + 'campground.png'
          }
        };

        var features = [
          {
            position: new google.maps.LatLng(11.02368110531636, 77.00253009796143),
            type: 'potholes'
          },{
            position: new google.maps.LatLng(11.038057916898168, 77.03770758256542),
            type: 'potholes'
          },{
            position: new google.maps.LatLng(11.026906181104199, 77.02227924334716),
            type: 'road_furniture'
          }, {
            position: new google.maps.LatLng(11.0148203513, 77.0236160564),
            type: 'road_sign'
          }, {
            position: new google.maps.LatLng(11.030678331460905, 77.0167635037908),
            type: 'road_furniture'
          },
          {
            position: new google.maps.LatLng(11.025787271795734, 77.01538324356079),
            type: 'potholes'
          },
          {
            position: new google.maps.LatLng(11.025050115243769, 77.01119899749756),
            type: 'road_furniture'
          },
          {
            position: new google.maps.LatLng(11.021111561787002, 76.99392557144165),
            type: 'road_sign'
          },
          {
            position: new google.maps.LatLng(11.022301558097276, 76.99972987174988),
            type: 'road_furniture'
          },
          {
            position: new google.maps.LatLng(11.019847843620942, 76.99221968650818),
            type: 'road_furniture'
          },
          {
            position: new google.maps.LatLng(11.04401668721413, 77.04674883076848),
            type: 'road_sign'
          },{
            position: new google.maps.LatLng(11.045501433384475, 77.05025716015996),
            type: 'potholes'
          }

        ];

        // Create markers.
        for (var i = 0; i < features.length; i++) {
          var marker = new google.maps.Marker({
            position: features[i].position,
            icon: icons[features[i].type].icon,
            map: map
          });
        };
      }
