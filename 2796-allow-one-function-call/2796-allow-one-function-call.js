/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let x=0
    return function(...args){
        if (x==0){
            x=1
            return fn(...args)
        }
        else{
            return undefined
        }
    }
};