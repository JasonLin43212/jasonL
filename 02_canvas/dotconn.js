/*
Team Lingo -- Kevin Lin, Jason Lin
SoftDev2 pd7
K02 -- ...Connecting the Dots
2019-02-01
*/
var c = document.getElementById('playground');
//Instantiate the context of the canvas
var ctx = c.getContext("2d");

//Get the buttons for clear and toggle and current mode
var clearButton = document.getElementById('clear');

//Add event listeners for clicking on canvas
c.addEventListener('click', (e) => {
    //Pass in the x and y coordinates of where the mouse draws inside of canvas relative to origin
    draw(e.offsetX,e.offsetY);
});

//Event listener for clearing
clearButton.addEventListener('click', (e) => {
    //Prevent default stops clicks from submitting or hyperlinking or having their default function
    //e.preventDefault();
    clearCanvas();
});


//Clears the canvas by starting at the origin and wiping out the width and height
var clearCanvas = () => {
    ctx.clearRect(0,0,c.width,c.height);
    ctx.beginPath();
    isClear = true;
    var prevX = -1;
    var prevY = -1;
};

var isClear = true;
var prevX = -1;
var prevY = -1;
//Draws rectangle or dot based on x and y
var draw = (x,y) => {
    ctx.beginPath();//Begins the path
    ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
    ctx.fillStyle = "#ff0000";
    ctx.fill();//Draws the dot by using an ellipse
    ctx.strokeStyle = "#000000"
    ctx.stroke();//Makes the border of the dot

    if (!isClear){
        ctx.beginPath();
        ctx.moveTo(prevX,prevY);//Start point at previous center
        ctx.lineTo(x,y);//End point at new cetner for line
        ctx.strokeStyle = "#006400"
        ctx.stroke();
    }
    prevX = x;
    prevY = y;
    isClear = false;//Tells the program that the user has draw first dot
};
