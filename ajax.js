var ajax = new XMLHttpRequest();
var word = 'сталь';
ajax.onreadystatechange = function() {
    console.log(this.responseText);
};
ajax.open('GET', 'script.py?word=' + word, true);
ajax.send();