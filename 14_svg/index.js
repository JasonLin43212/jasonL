//Testing Null elements
console.log(d3.selectAll("p").selectAll("span"));

//Testing adding one data only
console.log(d3.select("h2").datum(33));

//Bounding divs to an array of data
var data = [2,53,213,3];
console.log(d3.selectAll("div").data(data));

//Testing the name property
var letters = [
    {name: "A", frequency: .08167},
    {name: "B", frequency: .01492},
    {name: "C", frequency: .02780},
    {name: "D", frequency: .04253},
    {name: "E", frequency: .12702}
];

var letter= [
    {name: "D"},
    {name: "A"},
    {name: "B"},
    {name: "C"},
    {name: "E"}
];

function name(d) {
    return d.name;
}

var select = d3.selectAll("span").data(letter).data(letters,name);
console.log(select);
var i;
for (i=0;i<5;i++){
    console.log(select["_groups"][0][i]["__data__"]);
}
