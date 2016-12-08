const fs = require('fs');
const file = fs.readFileSync('data', 'utf8');
// const file = `aaaaa-bbb-z-y-x-123[abxyz]
// a-b-c-d-e-f-g-h-987[abcde]
// not-a-real-room-404[oarel]
// totally-real-room-200[decoy]`

function part1() {
    const inputs = file.split('\n');
    // inputs.pop();
    const rooms = inputs.filter(input=>input).map(input=>extractData(input));
    let sum = 0;
    rooms.forEach((room, index)=>{
        if (isRealRoom(room)) {
            sum += room.id;
            console.log(inputs[index]);
        }
    })
    console.log(sum);
}

function extractData(str) {
    const data = str.split('-');
    const IdAndChecksum = data.pop().split('[');
    const id = Number(IdAndChecksum[0]);
    const checksum = IdAndChecksum[1].slice(0, -1);
    return { data, id, checksum };
}

function isRealRoom(room) {
    let charset = {};
    let chars = room.data.join('').split('');
    chars.forEach(char => {
        charset[char] = charset[char] || 0;
        charset[char] += 1;
    })
    let array =
        Object.keys(charset)
        .map(key=>{
            return {key: key, value: charset[key]};
        }).sort((a, b) => {
            if (a.value == b.value) {
                return a.key > b.key;
            } else {
                return a.value < b.value;
            }
        });
    let toCheck = '';
    for (let i = 0; i < 5; i++) {
        toCheck += array[i].key;
    }
    return toCheck == room.checksum;
}

// console.log(isRealRoom(extractData('aaaaa-bbb-z-y-x-123[abxyz]')));
// console.log(isRealRoom(extractData('a-b-c-d-e-f-g-h-987[abcde]')));
// console.log(isRealRoom(extractData('not-a-real-room-404[oarel]')));
// console.log(isRealRoom(extractData('totally-real-room-200[decoy]')));


part1();
