const fs = require('fs');
let input = fs.readFileSync('data', 'utf8');
const reg = /\(\d+x\d+\)/;

function decatch(cc) {
    cc = cc.substring(1, cc.length - 1);
    return cc.split('x').map(Number);
}

// input = 'A(2x2)BCD(2x2)EFG';

let c = input.match(reg);
while (c) {
    c = c[0];
    const index = input.match(reg).index;
    const [len, times] = decatch(c);
    const start = index + c.length;
    toReplacePart = input.substring(start, start + len);
    toReplace = '';
    
    for (let i = 0; i < times - 1; i++) {
        toReplace += toReplacePart;
    }

    input = input.replace(c, toReplace);

    c = input.match(reg);
}

console.log(input.length);