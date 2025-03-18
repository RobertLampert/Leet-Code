function isPalindrome(s) {
    s = s.toLowerCase();
    var origString = s;
    for (var _i = 0, s_1 = s; _i < s_1.length; _i++) {
        var char = s_1[_i];
        if (!/^[a-z0-9]+$/i.test(char)) {
            s = s.replace(char, "");
        }
    }
    var startPointer = 0;
    var endPointer = s.length - 1;
    for (var i = 0; i < s.length; i++) {
        // console.log("left pointer is: " + s[startPointer]+ " right pointer is: " + s[endPointer])
        if (s[startPointer] != s[endPointer]) {
            return false;
        }
        startPointer++;
        endPointer--;
    }
    return true;
}
;
var testString1 = "A man, a plan, a canal: Panama";
var testString2 = "race a car";
var testString3 = " ";
console.log(isPalindrome(testString1));
console.log(isPalindrome(testString2));
console.log(isPalindrome(testString3));
