const fs = require('fs');
const a = fs.readFileSync('data', 'utf8');
const inputs = a.split('\n');
let result = 0;
let count = 0;
let first = [], second = [], third = [];
inputs.forEach(input => {
    const lines = input.split(' ').filter(num=>num).map(num=>Number(num));
    first[count] = lines[0];
    second[count] = lines[1];
    third[count] = lines[2];
    if (count == 2) {
        count = -1;
        [first, second, third].forEach(tran=>{
            if (isTran(tran)) {
                result += 1;
            }
        })
    }
    count += 1;
})
console.log(result);

function isTran(tran) {
    tran = tran.sort((a,b) => a - b);
    let a, b, c;
    a = tran[0];
    b = tran[1];
    c = tran[2];
    return a + b > c;
}
