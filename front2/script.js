$(document).ready(function(){
    console.log('worked');

    $.ajax({
        method:'GET',
        url:'http://127.0.0.1:8000/api/game/',
        success:function(response){
            var myData =response;
            console.log(myData);
            console.log(myData.count)
            buildTable(myData);
        }
    })

});





function buildTable(data){
    var table = document.getElementById('game_table_data');

    for (var i = 0; i < data.count;i++){
        console.log(i)
        var row =   `<tr>
                        <td>${data['results'][i].game_id}</td>            
                        <td>${data['results'][i].name}</td>            
                        <td>${data['results'][i].release_date}</td>            
                        <td><img src="${data['results'][i].game_img}"</td>            
                    </tr>`;
        console.log(row)
        table.innerHTML += row;
    }

}


function addHeaders(table, keys) {
    var row = table.insertRow();
    for( var i = 0; i < keys.length; i++ ) {
      var cell = row.insertCell();
      cell.appendChild(document.createTextNode(keys[i]));
    }
  }
  
  var table = document.createElement('table');
  for( var i = 0; i < children.length; i++ ) {
  
    var child = children[i];
    if(i === 0 ) {
      addHeaders(table, Object.keys(child));
    }
    var row = table.insertRow();
    Object.keys(child).forEach(function(k) {
      console.log(k);
      var cell = row.insertCell();
      cell.appendChild(document.createTextNode(child[k]));
    })
  }

  document.getElementById('test').appendChild(table);