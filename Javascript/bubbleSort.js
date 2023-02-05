function bubble(arr) {
    let j = 0;
    let ii = 0;
    let x = 0;
    for (let i = 0; i < Math.pow(arr.length, 2); i++) {
        if (j >= arr.length-1) j = 0;
        if (ii >= arr.length-1) ii = 0;
        j = ii + 1;
        if (arr[ii] > arr[j]) {
            x = arr[ii];
            arr[ii] = arr[j];
            arr[j] = x;
        }
        ii++;
    }
    return arr;
}

console.log(buble([5,2,7,1,8,6,3,4,9,7,7,7,7,77,7,7,7,7,5,4,54344,23,5,3,5,5,3,2,2,543,25,56,33,643,221,32,321,32,1]));