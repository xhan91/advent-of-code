const fs = require('fs');
const inputs = fs.readFileSync('data', 'utf8');
const test = `eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar`;

function part1(inputs) {
    const array = inputs.split('\n');
    const result = [];
    // array.pop();
    array.forEach(word => {
        word.split('').forEach((value, index) => {
            result[index] = result[index] || {};
            result[index][value] = result[index][value] || 0;
            result[index][value] += 1;
        });
    });
    let word = result.map(map => {
        return Object.keys(map).reduce((a, b) => {
            return map[a] > map[b] ? a : b;
        })
    }).join('');
    console.log(word);
}

function part2(inputs) {
    const array = inputs.split('\n');
    const result = [];
    // array.pop();
    array.forEach(word => {
        word.split('').forEach((value, index) => {
            result[index] = result[index] || {};
            result[index][value] = result[index][value] || 0;
            result[index][value] += 1;
        });
    });
    let word = result.map(map => {
        return Object.keys(map).reduce((a, b) => {
            return map[a] < map[b] ? a : b;
        })
    }).join('');
    console.log(word);
}

part1(test);
part1(inputs);
part2(test);
part2(inputs);
