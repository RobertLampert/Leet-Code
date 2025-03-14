function isValid(s: string): boolean {
    const charArr: String[] = Array.from(s);
    const openingPar: String[] = ["{","[","("];
    const closingPar: String[] = ["}","]",")"];
    if(s.length % 2 != 0 || closingPar.includes(charArr[0]) ){
        return false;
    }
    for(let i: number = 0; i < charArr.length; i++){
        if(closingPar.includes(charArr[i])){
            let bracketNum = closingPar.lastIndexOf(charArr[i]);
            if(charArr[i-1] != openingPar[bracketNum]){
                return false;
            }else{
                charArr.splice(i-1,2);
                i -= 2;
            }
            
        }
    }
    if(charArr.length != 0){
        return false;
    }else{
        return true;
    }
};

const stringInput: string = "()[]{}";
console.log(isValid(stringInput));