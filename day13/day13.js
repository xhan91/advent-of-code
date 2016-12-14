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

function findThePath(map, x, y) {
    let found = false;
    let step = 0;
    let grey = [ { x: 1, y: 1 } ];
    while (!found) {
        grey.forEach(pos=>{
            let { x, y } = pos;
            
        })
    }
    let copy = JSON.parse(JSON.stringify(map));

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
