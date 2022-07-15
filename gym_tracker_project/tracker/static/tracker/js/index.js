var modal = document.getElementById("myModal");
var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
  }
window.onclick = function(event) {
if (event.target == modal) {
    modal.style.display = "none";
}
}
function myFunction() {
    var x = document.getElementById("id_name");
    console.log(x.value)
    
    if (x.value == "") {
        modal.style.display = "block";
    }
    if (x.value == "Bench Press") {
        console.log('here')
        document.getElementById("id_sets").defaultValue = "3";
        document.getElementById("id_reps").defaultValue = "10";
        document.getElementById("id_weight").defaultValue = "225";
    }
    
  }

function close() {
    modal.style.display = "none";
}