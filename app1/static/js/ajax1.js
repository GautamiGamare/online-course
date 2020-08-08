function ajaxCheck(req_url,id_name,span_id) {
    var student_data = document.getElementById(id_name).value;
    var pram = "data="+student_data;
    var request = new XMLHttpRequest();
    request.onreadystatechange = checkNum;
    request.open("POST",req_url,true)
    request.setRequestHeader('Content-Type','application/x-www-form-urlencoded')
    request.send(pram)
    function checkNum() {
        if (request.readyState===4)
        {   var value = request.responseText;
            var json_data = JSON.parse(value);
            var sp = document.getElementById(span_id);
            if(json_data.message === "Available")
            {
                sp.style.color = "green";
                sp.innerText = json_data.message;
                document.getElementById("btn1").disabled = false;
            }
            else {
                sp.style.color = "red";
                sp.innerText = json_data.error;
                document.getElementById("btn1").disabled = true;
            }
        }
}
}