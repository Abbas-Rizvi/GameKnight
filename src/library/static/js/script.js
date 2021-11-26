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
        var url = ("/library/game/" + data['results'][i].game_id);
        var row =   `<tr>
                        <td>${data['results'][i].game_id}</td>            
                        <td><a href=${url}>${data['results'][i].name}</a></td>            
                        <td>${data['results'][i].release_date}</td>            
                        <td><img src="${data['results'][i].game_img}"</td>            
                    </tr>`;
        console.log(row)
        table.innerHTML += row;
    }

}
