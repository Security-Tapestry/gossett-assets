var key = "G0$$@m3r"
(function keyHole() {
    var lock = prompt("Wings?");
    while (lock !== key) {
        alert("Access Denied");
        return keyHole();
    }
}());
alert('Welcome, Gossett Motors');