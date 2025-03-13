function twoSum(nums: number[], target: number): number[] {
    const length: number = nums.length;
    let targetIndices: number[] = [];
    const newmap = new Map<number, number>();
    for(let i:number=0; i < length; i++){
        newmap.set(nums[i], i);
    }
    for(let i:number=0; i < length; i++){
        const complement = target - nums[i];
        if (newmap.has(complement) && newmap.get(complement) !== i){
            targetIndices.push(i);
            targetIndices.push(newmap.get(complement)!);
            return targetIndices;
        }
    }
    return targetIndices;
};

let testNumbers: number[] = [3,2,4];
console.log(twoSum(testNumbers,6));