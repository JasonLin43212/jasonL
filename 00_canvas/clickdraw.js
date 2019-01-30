var c = document.getElementById('slate');
//Instantiate the context of the canvas
var ctx = c.getContext("2d");

//Sets the state to rectangle. The other mode is dot.
var state = "rectangle";

//Get the buttons for clear and toggle and current mode
var clearButton = document.getElementById('clear');
var toggleButton = document.getElementById('toggle');

//Add event listeners for clicking on button and canvas
c.addEventListener('click', (e) => {
    console.log(e);
});

clearButton.addEventListener('click', (e) => {
    clearCanvas();
});

toggleButton.addEventListener('click', (e) => {
    console.log(e);
});

var clearCanvas = () => {
    console.log("clear");
    ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);
};
//console.log(clearButton);
//console.log(toggleButton);
