const fs = require('fs');
const file = fs.readFileSync('data', 'utf8');

function extractData(str) {
    const data = str.split('-');
    const IdAndChecksum = data.pop().split('[');
    const id = Number(IdAndChecksum[0]);
    const checksum = IdAndChecksum[1].slice(0, -1);
    return { data, id, checksum };
}

function isRealRoom(room) {
    return false;
}

function part1() {
    const inputs = file.split('\n');
    inputs.pop();
    b = inputs.map(input=>extractData(input));
    console.log(b);
}

part1();
