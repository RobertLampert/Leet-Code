function twoSum(nums: number[], target: number): number[] {
    const length: number = nums.length;
    let targetIndices: number[] = [];
    for(let i: number = 0; i < length; i++){
        for(let j: number = 0; j < length; j++){
            if( nums[i] + nums[j] == target && i != j){
                targetIndices.push(i);
                targetIndices.push(j);
                return targetIndices;
            }
        }
    }
    return targetIndices;
};

let testNumbers: number[] = [3,2,4];
console.log(twoSum(testNumbers,6));