function filterHostname() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("hostnameSearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("assets");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[14];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function filterSerial() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("serialSearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("assets");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[4];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function filterMAC() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("macSearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("assets");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[12];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

function filterIP() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("ipSearch");
    filter = input.value.toUpperCase();
    table = document.getElementById("assets");
    tr = table.getElementsByTagName("tr");
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[15];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}