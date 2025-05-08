/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const operations = {
        plusone: function(arr) {
            for (let i = 0; i < arr.length; i++) {
                arr[i] += 1;
            }
            return arr;
        },
        plusI: function(arr, i) {
            for (let j = 0; j < arr.length; j++) {
                arr[j] += i;
            }
            return arr;
        },
        constant: function() {
            for (let i = 0; i < arr.length; i++) {
                arr[i] = 42;
            }
            return arr;
        }
    };
    if (typeof fn == "function") {
        let result = [];
        for (let i = 0; i < arr.length; i++) {
            result.push(fn(arr[i], i));
        }
        return result;
    };
};