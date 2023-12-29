// normal
function addNums0(num1 = 1, num2 = 1){
    return num1 + num2;
}
const addNums = (num1 = 1, num2 = 1) => {
    console.log(num1 + num2);
}
const addNums1 = (num1 = 1, num2 = 1) => console.log(num1 + num2);
const addNums2 = (num1 = 1, num2 = 1) => num1 + num2;
const addNums3 = (num1 = 1, num2 = 1) => {
    return num1 + num2;
}
const addNums4 = num1 => num1 + 5;
const addNums5 = (num1 = 1, num2 = 1) => num1 + num2;

console.log(addNums0(5, 5));
addNums(5, 5);
addNums1(5, 5);
console.log(addNums2(5, 5));
console.log(addNums3(5, 5));
console.log(addNums4(5, 5));
