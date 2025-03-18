function isPalindrome(s: string): boolean {
    const formattedString: string = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    let startPointer = 0;
    let endPointer = formattedString.length-1;
    while(startPointer < endPointer){
        if(formattedString.charAt(startPointer) !== formattedString.charAt(endPointer)){
            return false;
        }
        startPointer++;
        endPointer--;
    }
    return true;
};


let testString1: string = "A man, a plan, a canal: Panama";
const testString2: string = "race a car";
const testString3: string = " ";
console.log(isPalindrome(testString1));
console.log(isPalindrome(testString2));
console.log(isPalindrome(testString3));