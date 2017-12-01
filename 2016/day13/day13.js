// we want to go 31, 39; so let's draw a map of 40 x 40
function drawTheMap(puzzleInput) {
    const map = [];
    for (let i = 0; i < 40; i++) {
        // x
        map[i] = [];
        for (let j = 0; j < 40; j++) {
            // y
            let num = i * i + 3 * i + 2 * i * j + j + j * j;
            num += puzzleInput;
            num = num.toString(2);
            num = num.split('');
            let count = 0;
            num.forEach(digit=>{
                if (digit === '1') {
                    count += 1;
                }
            });
            map[i][j] = count % 2 === 1 ? '#' : '.';
        }
    }
    return map;
}

function findThePath(_map) {
    let found = false;
    let step = 0;
    let grey = [ { x: 1, y: 1 } ];
    let map = _map;
    map[1][1] = 'O';

    while (!found) {
        let copy = JSON.parse(JSON.stringify(map));
        let newGrey = [];
        step += 1;
        grey.forEach(pos => {
            if (found) return;
            let {x, y} = pos;
            f1 = checkAndPushToGrey(map, copy, x+1, y, newGrey);
            f2 = checkAndPushToGrey(map, copy, x-1, y, newGrey);
            f3 = checkAndPushToGrey(map, copy, x, y+1, newGrey);
            f4 = checkAndPushToGrey(map, copy, x, y-1, newGrey);
            found = f1 || f2 || f3 || f4;
        });
        map = copy;
        grey = newGrey;
    }

    console.log(step);
}

function checkAndPushToGrey(map, copy, x, y, grey) {
    if (checkPoint(map, x, y)) {
        copy[x][y] = 'O';
        grey.push({x: x, y: y});
    }
    // This is checking if the des is found, should be passed value instead of hardcoding.
    return (x === 31 && y === 39 );
}

function checkPoint(map, x, y) {
    if (x >= 0 && y >= 0) {
        return map[x][y] === '.';
    }
    return false;
}

// For visualization
function printTheMap(map, width, height) {
    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x ++) {
            process.stdout.write(`${map[x][y]}`);
        }
        console.log('');
    }
}

// the test data
// const map = drawTheMap(10);
// printTheMap(map, 10, 7);
findThePath(drawTheMap(1362));
