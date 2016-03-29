var metadata;
var labels;

$.get('/metadata', function(data) {
    console.log(data);
    metadata = JSON.parse(data);
    labels = metadata.labels;
});

document.getElementById('submit').onclick = function() {
    var userData = [];
    for (var i in labels) {
        var inputVal = document.getElementById(labels[i]).value;
        userData.push(inputVal);
    }
    console.log(userData);
    $.get('/predict', {'values': userData}, function(data) {
       console.log(data);
       document.getElementById('result').innerHTML = "<p>" + data + "</p>";
    });
    return false;
};

