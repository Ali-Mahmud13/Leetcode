/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        let result = x;
        // Loop through the functions array in reverse
        for (let i = functions.length - 1; i >= 0; i--) {
            result = functions[i](result); // Apply each function to the result
        }
        return result;
    };
};

/**
 * Example usage:
 * const fn = compose([x => x + 1, x => 2 * x]);
 * console.log(fn(4)); // Output: 9
 */


/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */