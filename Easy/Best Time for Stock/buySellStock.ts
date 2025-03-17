function maxProfit(prices: number[]): number {
    let currentMax: number = 0;
    for(let i: number = 0; i < prices.length; i++){
        for(let j: number = i+1; j < prices.length;j++){
            if(prices[i]<prices[j] && prices[j]-prices[i] > currentMax){
                currentMax = prices[j]-prices[i];
            }
        }
    }
    return currentMax;
};

const prices: number[] = [1,2,3,4,5];
console.log(maxProfit(prices));