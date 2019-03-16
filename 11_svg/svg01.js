/*
Jason Lin
SoftDev2 Pd7
K11 -- Ask Circles [Change || Die] …While On The Go
2019-03-16
*/

var pic = document.getElementById("vimage");
// Bind all buttons to a variable
var clearButton = document.getElementById("but_clear");
var moveButton = document.getElementById("but_move");
var stopButton = document.getElementById("but_stop");
var speedButtonX = document.getElementById("but_speed_x");
var slowButtonX = document.getElementById("but_slow_x");
var speedButtonY = document.getElementById("but_speed_y");
var slowButtonY = document.getElementById("but_slow_y");

var requestID;

// Draws a dot by setting the attributes first and then adding it to vimage
var draw_dot = function(x,y) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute( "cx", x );
    c.setAttribute( "cy", y );
    c.setAttribute( "r", "20" );
    c.setAttribute( "fill", "#0000ff" );
    c.addEventListener('click', circle_action);
    c.setAttribute( "velX", 2);
    c.setAttribute( "velY", 2);
    pic.appendChild( c );

}

// Changes color if blue, but if green, teleports the circle
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

// Removes all children of svg by deleting HTML
var clear = function() {
    pic.innerHTML = "";
}

// Draws a dot onto svg
var draw = e => {
    event.preventDefault(); //Stops click action from being executed
    var x = event.offsetX; //X cor of mouse
    var y = event.offsetY; //Y cor of mouse
    if (e.target.getAttribute("id") == "vimage"){
        draw_dot(x,y);
    }
}

// Animates the dots using requestAnimationFrame and checking if the future position
// is out of bounds. Must convert to integer to change velocities
var move_dots = () => {
    var i;
    var all_circles = pic.children;
    for (i=0; i<all_circles.length; i++){
        var a_circle = all_circles[i];
        var velX = parseInt(a_circle.getAttribute("velX"));
        var velY = parseInt(a_circle.getAttribute("velY"));
        var cx = parseInt(a_circle.getAttribute("cx"));
        var cy = parseInt(a_circle.getAttribute("cy"));

        if (cx + velX > pic.getAttribute("width") - 20 || cx + velX < 20){
            a_circle.setAttribute("velX",-1*velX);
        }
        if (cy + velY > pic.getAttribute("height") - 20 || cy + velY < 20){
            a_circle.setAttribute("velY",-1*velY);
        }
        velX = parseInt(a_circle.getAttribute("velX"));
        velY = parseInt(a_circle.getAttribute("velY"));
        a_circle.setAttribute("cx",cx + velX);
        a_circle.setAttribute("cy",cy + velY);
    }
    requestID = window.requestAnimationFrame(move_dots);//Get the id of the request to use for canceling
}

// Stops the current request ID
var stop = () => {
    window.cancelAnimationFrame(requestID);
}

// Changes the speed
var adjustSpeed = (direction, increment) => {
    var i;
    var all_circles = pic.children;
    for (i=0; i<all_circles.length; i++){
        var a_circle = all_circles[i];
        var velX = parseInt(a_circle.getAttribute("velX"));
        var velY = parseInt(a_circle.getAttribute("velY"));
        // X velocity. Checks if the future velocity is too big or too small
        if (direction === "x" && Math.abs(velX)+increment <= 20 && Math.abs(velX)+increment > 0){
            if (velX > 0){
                velX += increment;
            }
            // If velocity is negative, will subtract instead to get desired affect
            else {
                velX -= increment;
            }
        }
        // Y velocity. Checks if the future velocity is too big or small
        if (direction === "y" && Math.abs(velY)+increment <= 20 && Math.abs(velY)+increment > 0){
            if (velY > 0){
                velY += increment;
            }
            else {
                velY -= increment;
            }
        }
        a_circle.setAttribute("velX",velX);
        a_circle.setAttribute("velY",velY);
    }
}

// Stops the previous animation frame and starts a new one
var move = e => {
    stop();
    move_dots();
}

// Adding event listeners to buttons and svg
clearButton.addEventListener('click', clear);
moveButton.addEventListener('click', move);
stopButton.addEventListener('click', stop);
speedButtonX.addEventListener('click', () => {adjustSpeed("x",1)});
slowButtonX.addEventListener('click', () => {adjustSpeed("x",-1)});
speedButtonY.addEventListener('click', () => {adjustSpeed("y",1)});
slowButtonY.addEventListener('click', () => {adjustSpeed("y",-1)});
pic.addEventListener('click', draw);
