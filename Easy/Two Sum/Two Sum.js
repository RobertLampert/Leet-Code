function twoSum(nums, target) {
    var length = nums.length;
    var targetIndices = [];
    for (var i = 0; i < length; i++) {
        for (var j = 0; j < length; j++) {
            if (nums[i] + nums[j] == target && i != j) {
                targetIndices.push(i);
                targetIndices.push(j);
                return targetIndices;
            }
        }
    }
    return targetIndices;
}
;
var testNumbers = [3, 2, 4];
console.log(twoSum(testNumbers, 6));
