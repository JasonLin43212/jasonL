/*
Jason Lin
SoftDev2 Pd7
K10 -- Ask Circles [Change || Die]
2019-03-13
*/

var pic = document.getElementById("vimage");
var clearButton = document.getElementById("but_clear");
var moveButton = document.getElementById("but_move");

var draw_dot = function(x,y) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute( "cx", x );
    c.setAttribute( "cy", y );
    c.setAttribute( "r", "20" );
    c.setAttribute( "fill", "#0000ff" );
    c.addEventListener('click', circle_action);
    pic.appendChild( c );

}

var circle_action = e => {
    if (e.target.getAttribute("fill") === "#0000ff"){
        e.target.setAttribute("fill","#00ff00");
    }
    else {
        pic.removeChild(e.target);
        newX = Math.floor(Math.random() * pic.getAttribute("width"));
        newY = Math.floor(Math.random() * pic.getAttribute("height"));
        draw_dot(newX,newY);
    }
}

var clear = function() {
    while (pic.firstChild) { // Removes all children while there are children
        pic.removeChild(pic.firstChild);
    }
}

var draw = e => {
    event.preventDefault(); //Stops click action from being executed
    var x = event.offsetX; //X cor of mouse
    var y = event.offsetY; //Y cor of mouse
    if (e.target.getAttribute("id") == "vimage"){
        draw_dot(x,y);
    }
}

clearButton.addEventListener('click', clear);
pic.addEventListener('click', draw);
