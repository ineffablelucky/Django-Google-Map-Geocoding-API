var map;

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

    map.addListener('click', function(e) {

        var marker
        marker = new google.maps.Marker({
        position: e.latLng,
        map: map
        });


    });

}



