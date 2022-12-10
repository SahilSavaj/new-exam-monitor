function value_setter(id){
    var submit = document.getElementById("submit_button")
    
    if (submit.classList.length == 0){
        submit.classList.add('done');
        console.log('here!')
        submit.disabled = false;
    }

    var option = document.getElementById(id);
    option.value = id;
 
    var options =  ["A","B","C","D"];
    var index = options.indexOf(id);
    options.splice(index,1);
    let temp = document.getElementById(options[0]);
    temp.value = "0";
    temp = document.getElementById(options[1]);
    temp.value = "0";
    temp = document.getElementById(options[2]);
    temp.value = "0";   

 }


