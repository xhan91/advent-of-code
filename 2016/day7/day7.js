const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');

function part1() {
    let count = 0;
    console.log(inputs.split('\n').length);
    inputs.split('\n').forEach(input=>{
        if (isIp(input)) {
            // console.log(input);
            count += 1;
        }
    })
    return count;
}

function isIp(string) {
    let insides = string.match(/\[\w+\]/g);
    // console.log(insides);
    for (i in insides) {
        if (hasABBA(insides[i])) {
            return false;
        }
    }
    return hasABBA(string);
}

function hasABBA(string) {
    const abba = /(\w)([^\1])\2\1/;
    const aaaa = /(\w)\1{3}/;
    return abba.test(string) && !aaaa.test(string);
}

console.log(part1());
// got 117 and the answer is 118, why
