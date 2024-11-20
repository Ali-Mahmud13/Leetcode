/**
 * @param {string|number|boolean} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(expected) {
             if (val !== expected) {
                throw new Error("Not Equal"); // Throws error if values are equal 
            }
            return true;
        },
        notToBe: function(expected) {
            if (val === expected) {
                throw new Error("Equal"); // Throws error if values are equal
            }
            return true; // Otherwise returns true
        }
    };
};


/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */