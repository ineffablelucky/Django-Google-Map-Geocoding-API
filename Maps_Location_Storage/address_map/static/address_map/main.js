var map;
var coordinates;
var componentForm = {
        locality: 'long_name',
        administrative_area_level_1: 'short_name',
        country: 'long_name'
    };


$(document).on('click','#add_address', function() {

        $('#create_map').modal('show');
        initMap();

});


function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: 28.5355, lng: 77.3910},
          zoom: 12
    });

    var marker1 = new google.maps.Marker({
            position: {lat: 28.5830, lng: 77.3132},
            map: map,
            icon: 'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
    });

    var marker = new google.maps.Marker({
        position: {lat: 28.5355, lng: 77.3910},
        map: map
       });

    var geocoder = new google.maps.Geocoder


    map.addListener('click', function(e) {

        marker.setMap(null);

        var marker_new = new google.maps.Marker({
            position: e.latLng,
            map: map
        });

        marker = marker_new;

        coordinates = {lat: parseFloat(e.latLng.lat()), lng: parseFloat(e.latLng.lng())}

        geocoder.geocode({'location': coordinates}, function(results, status) {

                        if (status === 'OK') {

                            if (results[0]) {

                                $('#add_address').val(results[0].formatted_address);
                                $('#add_lat').val(coordinates.lat);
                                $('#add_lng').val(coordinates.lng);
                                Auto_fill_Address(results[0]);

                            } else {
                                window.alert('No results found');
                            }

                        } else {
                            window.alert('Geocoder failed due to: ' + status);
                        }
        });

    });

 }

function Auto_fill_Address(result){

    for (var i = 0; i < result.address_components.length; i++) {

          var addressType = result.address_components[i].types[0];

          if (componentForm[addressType]) {

            var val = result.address_components[i][componentForm[addressType]];
            document.getElementById(addressType).value = val;

          }
    }

 }
