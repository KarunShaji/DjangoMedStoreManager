var message_timeout = document.getElementById("message-timer");

setTimeout(function() {
    
    message_timeout.style.opacity = "0";
    setTimeout(function() {
        message_timeout.style.display = "none";
    }, 500);
}, 5000);



$(document).ready(function() {
    $("#confirmDeleteBtn").click(function() {
        $("#deleteForm").submit();
    });
});