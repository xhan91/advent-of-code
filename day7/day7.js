const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');

function part1() {
    let count = 0;
    console.log(inputs);
    inputs.split('\n').forEach(input=>{
        if (isIp(input)) {
            count += 1;
        }
    })
    return count;
}

function isIp(string) {
    let insides = string.match(/\[\w+\]/g);
    console.log(insides);
    for (i in insides) {
        console.log(i);
        console.log(hasABBA(insides[i]));
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

// console.log(isIp("abba[mnop]qrst"));
// console.log(isIp("abcd[bddb]xyyx"));
// console.log(isIp("aaaa[qwer]tyui"));
// console.log(isIp("ioxxoj[asdfgh]zxcvbn"));
// console.log(part1());
console.log(isIp("pncauthrouncvjkrik[cyiovjnoesdgpeyjpvd]ajhonypsbifeghxi[wmudcxwbewumjbegnh]qetzbstgmzfruzxqln"));
