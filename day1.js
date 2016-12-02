var question = "L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5";

function day1(str) {

    let aLeft = 0;
    let aUp = 0;
    let facing = 0;
    // u r d l // R +1; L -1

    let array = str.split(', ');
    array.forEach(param=>{
        let d = param.slice(0, 1);
        let value = Number(param.slice(1));
        if (d === 'L') {
            facing = facing - 1;
        } else {
            facing = facing + 1;
        }

        // MARK: used to use %4 and did not work
        if (facing === -1) {
            facing += 4;
        }
        if (facing === 4) {
            facing -= 4;
        }

        facing = facing % 4;
        switch (facing) {
            case 0:
                aUp += value;
                break;
            case 1:
                aLeft -= value;
                break;
            case 2:
                aUp -= value;
                break;
            case 3:
                aLeft += value;
                break;
            default:
                break;
        }
    });

    let distance = Math.abs(aLeft) + Math.abs(aUp);
    // console.log("aLeft: " + aLeft + ", aUp: " + aUp);
    // console.log("Distance: " + distance);
    return distance;
}

const assert = require('assert');

describe('day1', ()=>{
    it('should return 2 when input is \'R2, R2, R2\'', ()=>{
        assert.equal(day1('R2, R2, R2'), 2);
    });
    it('should return 12 when input is \'R5, L5, R5, R3\'', ()=>{
        assert.equal(day1('R5, L5, R5, R3'), 12);
    });
})

console.log("The result is: " + day1(question));
