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

//Add event listeners for clicking on button and canvas
c.addEventListener('click', (e) => {
    //Pass in the x and y coordinates of where the mouse draws inside of canvas
    var xCor = e.pageX - r.left;
    var yCor = e.pageY - r.top;
    draw(xCor,yCor);
});

clearButton.addEventListener('click', (e) => {
    clearCanvas();
});

toggleButton.addEventListener('click', (e) => {
    toggleMode();
});

//Clears the canvas by starting at the origin and wiping out the width and height
var clearCanvas = () => {
    ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);
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



var draw = (x,y) => {
    if (state === "box"){
        ctx.fillStyle = "#0000ff";
        ctx.fillRect(x,y,50,20);
    }
    else if (state === "dot"){
        ctx.fillStyle = "#ff0000";
        ctx.beginPath();
        ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
        ctx.fill();
    }
};
//console.log(clearButton);
//console.log(toggleButton);
