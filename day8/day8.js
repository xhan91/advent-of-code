const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');
var map;

function part1() {
    map = [];
    for (let i = 0; i < 6; i++) {
        map[i] = [];
    }
    console.log(map);
    const inputs = inputs.split('\n');
    inputs.forEach(operate);
}

function oeprate(str) {
    let commands = str.split(' ');
    if (commands.length < 1) return;
    switch (commands[0]) {
        case 'rect':
            rect(commands[1].split('x'));
            break;
        case 'rotate':
            rotate(commands[1], commands[2].slice(2), commands[4]);
            break;
        default:
            break;
    }
}

function rect(xy) {
    let [x, y] = xy;
}

function rotate(type, pos, value) {
    switch (type) {
        case 'row':
            
            break;
        case 'column':

            break;
        default:
            break;
    }
}

part1();
