function isPalindrome(s: string): boolean {
    s=s.toLowerCase();
    for(const char of s){
        if(!/^[a-z0-9]+$/i.test(char)){
            s=s.replace(char,"");
        }
    }
    let startPointer: number = 0;
    let endPointer: number = s.length-1;
    for(let i: number = 0; i < s.length; i++){
        // console.log("left pointer is: " + s[startPointer]+ " right pointer is: " + s[endPointer])
        if(s[startPointer] != s[endPointer]){
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