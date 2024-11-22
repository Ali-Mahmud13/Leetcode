/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArray=[];
    for (let i = 0; i < arr.length; i++) { // Properly declare `i` and fix syntax
        if (fn(arr[i], i)) { // Apply the `fn` function as a condition
            newArray.push(arr[i]); // Push the element to `newArray` if `fn` returns true
        }
    }
    return newArray;
    
};