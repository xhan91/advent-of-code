const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');
var map;

function part1() {
    init();
    const operations = inputs.split('\n');
    operations.forEach(operate);
    // this is actually part2
    printMap();
    countMap();
}

function init() {
    map = [];
    for (let i = 0; i < 50; i++) {
        map[i] = [];
        for (let j = 0; j < 6; j++) {
            map[i][j] = 0;
        }
    }
}

function operate(str) {
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
    for (let i = 0; i < x; i++) {
        for (let j = 0; j < y; j++) {
            if (map[i][j]) {
                map[i][j] = 0;
            } else {
                map[i][j] = 1;
            }
        }
    }
}

function rotate(type, _pos, _value) {
    let value = Number(_value);
    let pos = Number(_pos);
    let mapCopy;
    mapCopy = [];
    for (let i = 0; i < 50; i++) {
        mapCopy[i] = [];
        for (let j = 0; j < 6; j++) {
            mapCopy[i][j] = map[i][j];
        }
    }
    switch (type) {
        case 'row':
            for (let i = 0; i < 50; i++) {
                let des = (i + value) % 50;
                mapCopy[des][pos] = map[i][pos];
            }
            break;
        case 'column':
            for (let j = 0; j < 6; j++) {
                let des = (j + value) % 6;
                mapCopy[pos][des] = map[pos][j];
            }
            break;
        default:
            break;
    }
    map = mapCopy;
}

function printMap() {
    for (let j = 0; j < 6; j++) {
        //print a row
        for (let i = 0; i < 50; i++ ) {
            let print;
            if (map[i][j]) {
                print = '#';
            } else {
                print = '.';
            }
            process.stdout.write(`${print} `);
        }
        console.log('');
    }
}

function countMap() {
    let count = 0;
    for (let j = 0; j < 6; j++) {
        for (let i = 0; i < 50; i++) {
            count += map[i][j];
        }
    }
    console.log(count);
}

part1();
