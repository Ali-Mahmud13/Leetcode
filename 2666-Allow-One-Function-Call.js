/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called = false; // Track whether the function has been called

    return function(...args) {
        if (!called) {
            called = true; // Mark the function as called
            return fn(...args); // Call fn with the arguments and return the result
        }
        return undefined; // Return undefined for subsequent calls
    };
};


/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
