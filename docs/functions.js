function showList(){
    fetch("assets.json")
      .then(response => response.json())
      .then(data => createList(data));
}

function createList(data) {
    const mainUL = document.createElement('ol');
    for (let i = 0; i < data.result.length; i++) {
      const studentLI = document.createElement('li');
      studentLI.innerHTML = data.result[i].name;

      // create list for marks
      const marksUL = document.createElement('ul');
      for (var key in data.result[i].marks) {
        const marksLI = document.createElement('li');
        marksLI.innerHTML = key + ': ' + data.result[i].marks[key];
        marksUL.appendChild(marksLI);
      }

      // append marks list to studentLI
      studentLI.appendChild(marksUL);
      // append student list to mainUL
      mainUL.appendChild(studentLI);
    }
    // append mainUL to body
    document.body.appendChild(mainUL);
}