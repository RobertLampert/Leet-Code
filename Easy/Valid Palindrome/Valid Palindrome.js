function isPalindrome(s) {
    var formattedString = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    var startPointer = 0;
    var endPointer = formattedString.length - 1;
    while (startPointer < endPointer) {
        if (formattedString.charAt(startPointer) !== formattedString.charAt(endPointer)) {
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
