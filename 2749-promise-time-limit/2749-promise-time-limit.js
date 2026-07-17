/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
    return async function(...args) {
        const origP = fn(...args);
        const timeoutP = new Promise((_, reject) => {
            setTimeout(() => {reject('Time Limit Exceeded')}, t);
        })
        return Promise.race([origP, timeoutP]);
    }
};