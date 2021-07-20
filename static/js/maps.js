//Render Google Maps -- view_experience.html
let map;

//Get location data from experience
let lat = document.getElementById("lat").innerHTML;
let lng = document.getElementById("lng").innerHTML;

//Initialize map
function initMap() {
    //Parse lat into float
    xp_lat = parseFloat(lat);
    //Parse lng into float
    xp_lng = parseFloat(lng);
    //Store coordinates in variable
    let mapOptions = {
        center: {
            lat: xp_lat,
            lng: xp_lng
        },
        zoom: 11
    };

    //Center map on location
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    //Add marker to location
    my_position = {
        lat: xp_lat,
        lng: xp_lng
    }

    marker = new google.maps.Marker({
        position: my_position,
        map,
    });

    //Get data from experience
    let xp_name = document.getElementById("xp_name").innerHTML;
    let xp_location = document.getElementById("xp_location").innerHTML;

    //infowindow content
    let contentString = '<div style="text-align: center; font-weight: 400"><h6>'+ xp_name + '</h6><p>' + xp_location + '</p></div>';

    let infowindow = new google.maps.InfoWindow({
        content: contentString,
    });

    //Trigger infowindow on click
    marker.addListener("click", () => {
        infowindow.open({
            anchor: marker,
            map,
            shouldFocus: false,
        });
    });
}