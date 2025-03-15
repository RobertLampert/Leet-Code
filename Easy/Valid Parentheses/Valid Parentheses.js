function isValid(s) {
    var parMap = new Map([
        ["}", "{"],
        [")", "("],
        ["]", "["]
    ]);
    var openingPar = ["{", "[", "("];
    if (s.length % 2 != 0) {
        return false;
    }
    var stack = [];
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var char = s_1[_i];
        if (openingPar.includes(char)) {
            stack.push(char);
            console.log(stack);
        }
        else if (stack.length > 0 && parMap.get(char) == stack[stack.length - 1]) {
            stack.pop();
        }
        else {
            return false;
        }
    }
    if (stack.length == 0) {
        return true;
    }
    else {
        return false;
    }
}
;
var stringInput = "{([])}";
console.log(isValid(stringInput));
