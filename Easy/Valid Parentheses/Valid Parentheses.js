function isValid(s) {
    var charArr = Array.from(s);
    var openingPar = ["{", "[", "("];
    var closingPar = ["}", "]", ")"];
    if (s.length % 2 != 0 || closingPar.includes(charArr[0])) {
        return false;
    }
    for (var i = 0; i < charArr.length; i++) {
        if (closingPar.includes(charArr[i])) {
            var bracketNum = closingPar.lastIndexOf(charArr[i]);
            if (charArr[i - 1] != openingPar[bracketNum]) {
                return false;
            }
            else {
                charArr.splice(i - 1, 2);
                i -= 2;
            }
        }
    }
    if (charArr.length != 0) {
        return false;
    }
    else {
        return true;
    }
}
;
var stringInput = "()[]{}";
console.log(isValid(stringInput));
