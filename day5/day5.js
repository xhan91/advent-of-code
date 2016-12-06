const md5 = require('md5');
const question = 'ojvtpuvg';

function part1(question) {
    let index = 0;
    let result = '';
    while (result.length < 8) {
        let phase = question + index;
        let hash = md5(phase);
        if (isPassword(hash)) {
            result += hash[5];
            console.log(result);
        }
        index += 1;
    }
    return result;
}

function isPassword(string) {
    const validRegEx = /^00000[\dA-Fa-f]+/;
    return validRegEx.test(string);
}

function part2(question) {
    let index = 0;
    let result = [];
    while (!isFinished(result)) {
        let phase = question + index;
        let hash = md5(phase);
        if (isAdvancedPassword(hash)) {
            pos = hash[5];
            value = hash[6];
            result[pos] = result[pos] || value;
            console.log(result);
        }
        index += 1;
    }
    return result;
}

function isFinished(result) {
    return result[0] && result[1] && result[2] && result[3] && result[4] && result[5] && result[6] && result[7];
}

function isAdvancedPassword(string) {
    const validRegEx = /^00000[0-7][\dA-Fa-f]+/;
    return validRegEx.test(string);
}

// console.log(part2('abc'));
// console.log(part1(question));
// console.log(part2('abc'));
// console.log(part2(question));
