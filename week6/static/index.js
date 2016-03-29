var metadata;
var labels;

$.get('/metadata', function(data) {
    console.log(data);
    metadata = JSON.parse(data);
    labels = metadata.labels;
});

document.getElementById('submit').onclick = function() {
    var userData = {};
    for (var i in labels) {
        var inputVal = document.getElementById(labels[i]).value;
        userData[labels[i]] = inputVal;
    }
    console.log(userData);

    return false;
};

