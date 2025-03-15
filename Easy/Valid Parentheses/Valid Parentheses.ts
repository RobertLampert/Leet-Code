function isValid(s: string): boolean {
    const parMap = new Map<string, string>([
        ["}", "{"],
        [")", "("],
        ["]", "["]
      ]);

    const openingPar: String[] = ["{","[","("];

    if(s.length % 2 != 0){
        return false;
    }

    let stack: String[] = [];

    for(const char of s){
        if(openingPar.includes(char)){
            stack.push(char);
            console.log(stack);
        }else if(stack.length > 0 && parMap.get(char) == stack[stack.length -1]){
            stack.pop();
        }else{
            return false;
        }

    }

    if(stack.length==0){
        return true;
    }else{
        return false;
    }
};

const stringInput: string = "{([])}";
console.log(isValid(stringInput));