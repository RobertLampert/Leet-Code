function maxProfit(prices) {
    var currentMin = prices[0];
    var profitArr = [0];
    for (var i = 1; i < prices.length + 1; i++) {
        if (prices[i - 1] < currentMin) {
            currentMin = prices[i - 1];
            profitArr.push(profitArr[i - 1]);
        }
        else {
            if (profitArr[i - 1] < prices[i - 1] - currentMin) {
                profitArr.push(prices[i - 1] - currentMin);
            }
            else {
                profitArr.push(profitArr[i - 1]);
            }
        }
    }
    console.log(profitArr);
    console.log(currentMin);
    return profitArr[profitArr.length - 1];
}
;
var prices = [7, 1, 5, 3, 6, 4];
console.log(maxProfit(prices));
