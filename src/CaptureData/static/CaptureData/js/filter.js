var filterElements = document.querySelectorAll(".filter");
filterElements.forEach(function(filter) {
    filter.addEventListener("click", function() {
        var filterName = filter.getAttribute("data-filter-name");
        applyFilter(filterName);
    });
});

// AJAX function to apply the filter
function applyFilter(filterName) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/set-filter?filter-name=" + filterName, true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var overlay = document.getElementById("overlay");
            var image = overlay.querySelector("img");
            var timestamp = new Date().getTime();
            image.src = "/video?timestamp=" + timestamp;
        }
    };
    xhr.send();
}