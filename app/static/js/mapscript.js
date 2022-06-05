var map = L.map('leafletmap').setView([38.54220, -121.74960], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

var marker1 = L.marker([38.54220, -121.74960]).addTo(map);
marker1.bindPopup("<div class='mappopup'><b>University of California, Davis</b><br>I go to school here!</div>")