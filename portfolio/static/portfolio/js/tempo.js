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


    var name = document.querySelector('.name');
    var dataT = document.querySelector('.data');
    var icon = document.querySelector('.icon');
    var teste = document.querySelector('.teste');
    var temperatura = document.querySelector('.temperatura');

    fetch('https://api.weatherapi.com/v1/current.json?key=278b39c9618d4b4bb34230309221206&q=Lisbon&aqi=no')
    .then(response => response.json())
    .then(data => {
        console.log(data);

        dataT.innerHTML = data.location.name;
        icon.src = data.current.condition.icon;
        temperatura.innerHTML = data.current.temp_c + " °C";
        name.innerHTML = data.location.name;

    });