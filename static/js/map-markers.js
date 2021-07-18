"use strict";

function initMap() {
    const sfBayCoords= {
        lat: 37.601773,
        lng: -122.202287
    };

    const basicMap = new google.maps.Map(
        
    )

    const sfMarker = new google.maps.Marker({
        position: sfBayCoords,
        title: 'Headquarters',
        map: basicMap
    });