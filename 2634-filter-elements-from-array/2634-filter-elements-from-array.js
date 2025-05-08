/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let result = arr.filter(fn);
    const operations = {
        greaterThan10: function(n) {
            return arr.filter((num) => num > 10);
        },
        firstIndex: function(n, i) {
            return n[i];
        },
        plusOne: function(n) {
            return n.map(num => num + 1);
        }
    };
    if (operations[fn]) {
        return operations[fn](arr);
    };
    return result;
};