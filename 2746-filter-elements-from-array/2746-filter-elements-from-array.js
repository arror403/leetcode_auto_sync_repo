/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var res=[];
    for(let i=0; i<arr.length; i++){
        // console.log(typeof fn(arr[i], i))
        if (fn(arr[i], i)){
            res.push(arr[i]);
        }
    }
    return res;
};