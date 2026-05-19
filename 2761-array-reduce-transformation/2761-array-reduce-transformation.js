/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let L=nums.length
    if (L==0) return init
    
    let x=fn(init, nums[0])
    for(let i=1;i<L;i++){
        x=fn(x, nums[i])
    }
    return x
};