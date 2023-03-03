var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);


locations = []

// dealing with clicks in map
var popup = L.popup();

// Define the new marker icon
var newIcon = L.icon({
    iconUrl: 'assets/images/icon.png',
    iconSize: [32, 32]
});

function onMapClick(e) {
    if (locations.length == 0) {
        var marker = L.marker(e.latlng, { icon: newIcon }).addTo(map);
        locations.push(e.latlng)
    } else {
        var marker = L.marker(e.latlng).addTo(map);
        locations.push(e.latlng)
    }


}

map.on('click', onMapClick);

const button = document.querySelector('.btn');

button.addEventListener('click', () => {
    // console.log(locations)
    // send the data to the server
    fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "locations": locations })
    })
        .then(response => response.json())
        .then(data => console.log(data))
});
