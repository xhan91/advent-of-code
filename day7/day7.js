const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');

function part1() {
    let count = 0;
    let _inputs = inputs.split('\n');
    // _inputs.pop();
    console.log(_inputs);
    _inputs.forEach(input=>{
        if (isIp(input)) {
            count += 1;
        }
    })
    return count;
}

function isIp(string) {
    const a1 = string.split('[');
    const a2 = a1[1].split(']');
    const s1 = a1[0];
    const [s2, s3] = a2;
    // console.log(s1);
    // console.log(s2);
    // console.log(s3);
    return (hasABBA(s1) || hasABBA(s3)) && !hasABBA(s2);
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
console.log(part1());
