function time(){
    var currentTime = new Date();

    var hours = currentTime.getHours();
    var minutes = currentTime.getMinutes();
    var sec = currentTime.getSeconds();

    if (minutes < 10){
        minutes = "0" + minutes
    }
    if (sec < 10){
        sec = "0" + sec
    }
    var t_str = hours + ":" + minutes + ":" + sec + " ";

    if(hours > 11){
        t_str += "pm";
    } else {
       t_str += "am";
    }

     document.getElementById('currentTime').innerHTML = t_str;
     setTimeout(time,1000);

}