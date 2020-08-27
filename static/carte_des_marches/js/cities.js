map.on('click', 'unclustered-point', function(e) {
var coordinates = e.features[0].geometry.coordinates.slice();
var mag = e.features[0].properties.mag;
var tsunami;
 
if (e.features[0].properties.tsunami === 1) {
tsunami = 'yes';
} else {
tsunami = 'no';
}
 
// Ensure that if the map is zoomed out such that
// multiple copies of the feature are visible, the
// popup appears over the copy being pointed to.
while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
}
 
new mapboxgl.Popup()
.setLngLat(coordinates)
.setHTML(
'magnitude: ' + mag + '<br>Was there a tsunami?: ' + tsunami
)
.addTo(map);
});
 
map.on('mouseenter', 'clusters', function() {
map.getCanvas().style.cursor = 'pointer';
});
map.on('mouseleave', 'clusters', function() {
map.getCanvas().style.cursor = '';
});