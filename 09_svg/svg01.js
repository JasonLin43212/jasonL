/*
Jason Lin
SoftDev2 Pd7
K09 -- Connect the Dots
2019-03-13
*/

var pic = document.getElementById("vimage");
var clearButton = document.getElementById("but_clear");

var isClear = true; // Tells the program if there is no dots on screen
var prevX = null;
var prevY = null;

var draw_shapes = function(x,y) {

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute( "cx", x );
    c.setAttribute( "cy", y );
    c.setAttribute( "r", "10" );
    c.setAttribute( "fill", "#ff0000" );
    pic.appendChild( c );

    if (!isClear){

        var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l.setAttribute('x1', x);
        l.setAttribute('y1', y);
        l.setAttribute('x2', prevX);
        l.setAttribute('y2', prevY);
        l.setAttribute('stroke', "#000000");
        pic.appendChild( l );
    }
    prevX = x;
    prevY = y;
    isClear = false;//Tells the program that the user has draw first dot
}

var clear = function() {
    prevX = null;
    prevY = null;
    isClear = true;
    while (pic.firstChild) { // Removes all children while there are children
        pic.removeChild(pic.firstChild);
    }
}

var draw = e => {
    event.preventDefault(); //Stops click action from being executed
    var x = event.offsetX; //X cor of mouse
    var y = event.offsetY; //Y cor of mouse

    draw_shapes(x,y);
}

clearButton.addEventListener('click', clear);
pic.addEventListener('click', draw);
