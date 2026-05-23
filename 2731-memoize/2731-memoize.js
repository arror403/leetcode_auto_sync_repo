/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache={}
    
    return function(...args) {
        const key=JSON.stringify(args)

        if (key in cache){
            return cache[key]
        }

        const res=fn.apply(this, args)
        cache[key]=res

        return res
    }
}