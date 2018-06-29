/*
NOTE: most 'id' attributes are taken from django forms.py as form was initialized there, so
do check that file first if you are searching for any required id.
*/

var map;

var componentForm = { // object with 'id' of input form tag as keys which is same as data returned by google api ; used for auto-fill
        locality: 'long_name',
        administrative_area_level_1: 'short_name',
        country: 'long_name'
    };


$(document).on('click','#add_address', function() {

        $('#create_map').modal('show');
        initMap();

});

/*
NOTE: most 'id' attributes are taken from django forms.py as form was initialized there, so
do check that file first if you are searching for any required id.
*/
function initMap() {
    var latitude, longitude, marker;

    if (document.getElementById('add_lat').value === '') { // for create case
        latitude = 28.5355;
        longitude = 77.3910;
    } else { // for update case
        latitude = parseFloat(document.getElementById('add_lat').value);
        longitude = parseFloat(document.getElementById('add_lng').value);
    }

    map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: latitude, lng: longitude}, // Noida set as center
          zoom: 12
    });


    if (document.getElementById('add_address').value !== '') {

        marker = new google.maps.Marker({
        position: {lat: latitude, lng: longitude},
        map: map
       });

    }

    var geocoder = new google.maps.Geocoder

    map.addListener('click', function(e) {
        if(marker && marker.setMap){  // removing previous marker and creating new one
            marker.setMap(null);
        }

        marker = new google.maps.Marker({
            position: e.latLng,
            map: map
        });

        var coordinates = {lat: parseFloat(e.latLng.lat()), lng: parseFloat(e.latLng.lng())}

        geocoder.geocode({'location': coordinates}, function(results, status) {

                        if (status === 'OK') {

                            if (results[0]) {

                                $('#add_address').val(results[0].formatted_address);
                                $('#add_lat').val(coordinates.lat);
                                $('#add_lng').val(coordinates.lng);
                                Auto_fill_Address(results[0]);

                            } else {
                                window.alert('No address found');
                            }

                        } else {
                            window.alert('Geocoder failed due to: ' + status);
                        }
        });

    });

 }

/*
NOTE: most 'id' attributes are taken from django forms.py as form was initialized there, so
do check that file first if you are searching for any required id.
*/

function Auto_fill_Address(result){

    for (var i = 0; i < result.address_components.length; i++) {

          var addressType = result.address_components[i].types[0];

          if (componentForm[addressType]) {

                var val = result.address_components[i][componentForm[addressType]];
                document.getElementById(addressType).value = val;

          }
    }

 }
