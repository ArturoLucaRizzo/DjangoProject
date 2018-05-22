function search(e) {

    if (e.value.length > 0) {
            selectAll(e.value);


    }



}



function insert() {
    var x = document.getElementById("index");
    var y = document.getElementById("result");
    var button = document.getElementById("back");
    var listuser= document.getElementById("listuser");

        x.style.display = "none";
        y.innerHTML="";
        y.style.display = "block";

        button.style.display= "block"
        listuser.style.display = "none";


}
function back() {
    var x = document.getElementById("result");
    var y = document.getElementById("index");
    var button = document.getElementById("back");
    var listuser = document.getElementById("listuser");

        x.style.display = "none";
        y.style.display = "block";
        button.style.display= "none"
        listuser.style.display = "block";
}



function listuser() {
    var x = document.getElementById("index");
    var y = document.getElementById("result");
    var button = document.getElementById("back");
    var listuser= document.getElementById("listuser");

        x.style.display = "none";
        y.style.display = "block";
        button.style.display= "block"
        listuser.style.display = "none";

}

function selectAll(value){
    var values= value;
    options=""
    ActiveDTO={"value" : value}

    $.ajax({
			type: "POST",
			contentType : 'application/json; charset=utf-8',
			dataType : 'json',
			url: "/createJsonList",
            data: JSON.stringify(ActiveDTO) ,
            success :function(data) {
			    document.getElementById('list').innerHTML = "";
			       $.each(data.result, function(k,v) {
			             options += '<option value="' + v + '" />';
                   })
                   document.getElementById('list').innerHTML = options;
			}
		});


}



$(document).ready(function(){




$("#insert").click(function(e) {
    e.preventDefault();
    var name = document.getElementById("name").value;
    var surname = document.getElementById("surname").value;

    ActiveDTO={"name" : name, "surname" : surname,}

 $.ajax({
			type: "POST",
			contentType : 'application/json; charset=utf-8',
			dataType : 'json',
			url: "/readj",
            data: JSON.stringify(ActiveDTO) ,
            success :function(data) {
                if (data.result == "valid") {
                    document.getElementById('result').innerHTML = surname + " inserito correttamente nel db";

                }else if((data.result == "notValid") ){
                	document.getElementById('result').innerHTML = "Cognome gia presente nel DB";
				}



			}
		});

});

$("#listuser").click(function(e) {
    e.preventDefault();
    ActiveDTO={"listuser" : "lista"}

 $.ajax({
			type: "POST",
			contentType : 'application/json; charset=utf-8',
			dataType : 'json',
			url: "/listuser",
            data: JSON.stringify(ActiveDTO) ,
            success :function(data) {
                if (data.result == "valid") {
                    var lista="";
                    $.each(data.data.list, function(k,v) {
                        if (v.length<5){

                        }else{
                            lista=lista + v+"<br>";
                        }


                    });
                    document.getElementById('result').innerHTML = lista;

                }else if((data.result == "notValid") ){
                	document.getElementById('result').innerHTML = "Cognome gia presente nel DB";
				}



			}
		});

});

})