var map = L.map('leafletmap').setView([38.54220, -121.74960], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

var marker1 = L.marker([38.54220, -121.74960]).addTo(map).on("click", () => {
    document.getElementById('hobby1').scrollIntoView();
});

var marker2 = L.marker([21.085,-86.847]).addTo(map).on("click", () => {
    document.getElementById('hobby2').scrollIntoView();
});

var marker3 = L.marker([40.0139, -105.2748]).addTo(map).on("click", () => {
    document.getElementById('hobby3').scrollIntoView();
});

var marker4 = L.marker([55.9521, -3.1860]).addTo(map).on("click", () => {
    document.getElementById('hobby4').scrollIntoView();
});