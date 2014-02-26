$(document).ready(function() {

    

});

function get_terms() {
   $.ajax({
        type: 'GET',
        url: 'get_terms.php',
        dataType: 'json',
        success: function(data) {
            set_locations(data);
        }
   });
}

//maps
function set_locations(terms) {
    //var 
    for (term in terms) {
        $.ajax({
            type: 'GET',
            url: 'http://maps.googleapis.com/maps/api/geocode/json',
            address: term.name,
            key: 'AIzaSyAXjo2sX4q842CoC8QvdlvIP6nt2TJoVPg',
            success: function(data) {
                var location = data.results[0].geometry.location;
                var coordinates = [location.lat, location.lng].join(",");
                set_single_location(term, coordinates)
            }
        })
    }
}

function set_single_location(term, coordinates) {
    var term_updated = {
        id: term.id,
        name: term.name,
        location: coordinates
    };

    $.ajax({
        type: 'POST',
        url: 'set_location.php',
        data: term_updated,
        dataType: 'json',
        success: function(data) {
            console.log("Set coordinates for {" + term_updated.id 
                + "," + term_updated.name + "," + term_updated.location + "}");
        }
    });
}