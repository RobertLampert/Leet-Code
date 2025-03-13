function twoSum(nums, target) {
    var length = nums.length;
    var targetIndices = [];
    var newmap = new Map();
    for (var i = 0; i < length; i++) {
        newmap.set(nums[i], i);
    }
    for (var i = 0; i < length; i++) {
        var complement = target - nums[i];
        if (newmap.has(complement) && newmap.get(complement) !== i) {
            targetIndices.push(i);
            targetIndices.push(newmap.get(complement));
            return targetIndices;
        }
    }
    return targetIndices;
}
;
var testNumbers = [3, 2, 4];
console.log(twoSum(testNumbers, 6));
