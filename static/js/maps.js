//Render Google Maps
let map;

//Get location form experience
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
	    center: { lat: xp_lat, lng: xp_lng },
	    zoom: 13
	};

    //Center map on location
    map = new google.maps.Map(document.getElementById("map"), mapOptions);

    console.log(typeof xp_lat)
    console.log(xp_lat)
    console.log(typeof xp_lng)
    console.log(xp_lng)
}