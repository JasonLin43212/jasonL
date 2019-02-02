/*
Team Lingo -- Kevin Lin, Jason Lin
SoftDev2 pd7
K01 -- ...and I want to Paint It Better
2019-01-31
*/
var c = document.getElementById('slate');
//Instantiate the context of the canvas
var ctx = c.getContext("2d");

//Sets the state to rectangle. The other mode is dot.
var state = "box";
var mode = document.getElementById("mode");
mode.innerHTML = "Mode: Box";

//Get the buttons for clear and toggle and current mode
var clearButton = document.getElementById('clear');
var toggleButton = document.getElementById('toggle');

//Gets the canvas' origin for drawing
var r = c.getBoundingClientRect();

//Add event listeners for clicking on canvas
c.addEventListener('click', (e) => {
    //e.preventDefault();
    //Pass in the x and y coordinates of where the mouse draws inside of canvas relative to origin
    var xCor = e.offsetX;
    var yCor = e.offsetY;
    draw(xCor,yCor);
});

//Event listener for clearing
clearButton.addEventListener('click', (e) => {
    //Prevent default stops button from submitting or hyperlinking
    e.preventDefault();
    clearCanvas();
});

//Event listener for toggle
toggleButton.addEventListener('click', (e) => {
    //Prevent default stops button from submitting or hyperlinking
    e.preventDefault();
    toggleMode();
});

//Clears the canvas by starting at the origin and wiping out the width and height
var clearCanvas = () => {
    ctx.clearRect(0,0,c.width,c.height);
};

//Changes between the rectangle and dot mode of the drawing.
var toggleMode = () => {
    if (state === "box"){
        state = "dot";
        mode.innerHTML = "Mode: Dot";
    }
    else if (state === "dot"){
        state = "box";
        mode.innerHTML = "Mode: Box";
    }
}

//Draws rectangle or dot based on x and y
var draw = (x,y) => {
    if (state === "box"){
        ctx.fillStyle = "#0000ff";
        ctx.fillRect(x,y,50,20);
    }
    else if (state === "dot"){
        ctx.fillStyle = "#ff0000";
        ctx.beginPath();//Starts a new drawing path
        ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
        ctx.fill();//Fills in the path
    }
};
