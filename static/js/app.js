document.addEventListener("DOMContentLoaded", function() {
    const alertElement = document.getElementById("alert");

    if (alertElement) {
        // Set a timeout to add the 'hide' class after 3 seconds (adjust the time as needed)
        setTimeout(function() {
            alertElement.classList.add("hide");
        }, 3000);
    }
});
