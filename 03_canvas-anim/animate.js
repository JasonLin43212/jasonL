/*
Team Lingo -- Kevin Lin, Jason Lin
SoftDev2 pd7
K03 -- They lock us in the tower whenever we get caught
2019-02-04
*/

//Get the canvas element
var c = document.getElementById('playground');
//Instantiate the context of the canvas
var ctx = c.getContext("2d");

//Instantiate some variables for holding frame ID, radius and grow rate.
var requestID;
var radius = 1;
var growing = 1;

//Get the button elements for both animating and stopping.
var circleButton = document.getElementById('circle');
var stopButton = document.getElementById('stop');

ctx.fillStyle = "#bbbbbb";

var drawCircle = () => {
    clear();
    ctx.beginPath();//Starts a new path
    ctx.arc(c.width / 2, c.height / 2, radius, 0 , 2 * Math.PI);//Makes a full circle
    ctx.stroke();
    ctx.fill();//Fill in the circle
    //Once the circle reaches a certain point, it changes the growth rate
    if (radius >= c.width/2 || radius <= 0){
        growing *= -1;
    }
    radius += growing;
    requestID = window.requestAnimationFrame(drawCircle);//Get the id of the request to use for canceling
}

var clear = () => {
    ctx.clearRect(0,0,c.width,c.height);
}

//Cancels the last animation frame
var stopIt = () => {
    window.cancelAnimationFrame(requestID);
}

circleButton.addEventListener('click', () => {
    stopIt();//Prevents the button from speeding up the animation
    drawCircle();
});
stopButton.addEventListener('click',stopIt);
