/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Execute immediately
    fn(...args)
    // Start interval
    const intervalId = setInterval( () => {fn(...args)}, t)
    // Return cancel function
    return () => {clearInterval(intervalId)}
};