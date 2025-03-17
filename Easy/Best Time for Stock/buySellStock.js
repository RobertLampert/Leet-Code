function maxProfit(prices) {
    var currentMax = 0;
    for (var i = 0; i < prices.length; i++) {
        for (var j = i + 1; j < prices.length; j++) {
            if (prices[i] < prices[j] && prices[j] - prices[i] > currentMax) {
                currentMax = prices[j] - prices[i];
            }
        }
    }
    return currentMax;
}
;
var prices = [1, 2, 3, 4, 5];
console.log(maxProfit(prices));
