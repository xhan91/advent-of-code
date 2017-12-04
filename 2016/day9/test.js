const fs = require('fs');
let input = fs.readFileSync('data', 'utf8');

function decatch(cc) {
    cc = cc.substring(1, cc.length - 1);
    return cc.split('x').map(Number);
}

// input = 'A(2x2)BCD(2x2)EFG';
// input = 'X(8x2)(3x3)ABCY';
// input = '(6x1)(1x3)A';
input = 'A(1x5)BC';

let index = 0;
let sum = 0;
let openP = input.indexOf('(', index);

while (openP != -1) {
    sum += openP - index;
    let closeP = input.indexOf(')', index);
    const cat = input.substring(openP, closeP + 1);
    const [len, times] = decatch(cat);
    sum += len * times;
    index = closeP + len + 1;
    openP = input.indexOf('(', index);    
}

sum += input.length - index;

console.log(sum);