var MAPBOX_ID = 'airimia/cisp3edi900jx2xpep5gkt5fg';
var MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoiYWlyaW1pYSIsImEiOiJjaWtwaDl6Z3EwMGIydzltNG5mM2JyNTJxIn0.S0ASUcrn_e5_DwpwqA7vKw';

$(document).ready(function(){
    L.Icon.Default.imagePath = '../static/img/'
    var map = L.map('leaflet-map').setView([51.516120, -0.100027], 15);
    // disable scroll zoom so it doesn't interfere with page scroll
    // map.scrollWheelZoom.disable();

    // add Mapbox Streets tile layer
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/256/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        maxZoom: 17,
        id: MAPBOX_ID,
        accessToken: MAPBOX_ACCESS_TOKEN
    }).addTo(map);

    // set marker to point to given location
    L.marker([51.516120, -0.100027]).addTo(map);

    // show coordinates for clicks on the map
    var marker;
    function onMapClick(e) {
        marker = L.marker(e.latlng).addTo(map);
        marker.bindPopup("You clicked the map at " + e.latlng.toString()).openPopup();
    }

    function onPopupClose() {
        map.removeLayer(marker);
    }

    map.on('click', onMapClick);
    map.on('popupclose', onPopupClose);

    //Adding post when on click
    $(".navbar").on("click", '#nav-game', function(e){
        //$.post("game", url: '/signUpUser');
        $.ajax({
            url: '/game',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
        e.stopPropagation();
    });

});
