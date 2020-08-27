var request = new XMLHttpRequest();
request.open("GET", "{% static 'carte_des_marches/js/ardeche_cities.json' %}", false);
request.send(null)
var ardeche_cities = JSON.parse(request.responseText);

let features = [];
let id = 0;
ardeche_cities.forEach(function (city) {
    features.push(" {\n\"type\": \"Feature\", \"geometry\": {\"type\": \"Point\", \"coordinates\": ["+city.gps_lng+","+city.gps_lat+"]}, \"properties\": {'id': "+id+", \"department_code\": "+city.department_code+", \"zip_code\": "+city.zip_code+", 'name': "+city.name+"},\n");
});
export {features};
