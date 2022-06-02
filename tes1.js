// const a = 'ndakacm'
// const isPasswordValid = (value) => value.match(/^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$/)

// const b = isPasswordValid(a)

// console.log(b);

// const paragraph = 'The quick brown fox jumps over the lazy dog. It barked.';
// const regex = /[A-Z]/g;
// const found = paragraph.match(regex);

// console.log(found);
// expected output: Array ["T", "I"]


const paragraph = 'dakaScm2';
const regex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$/g;
const found = paragraph.match(regex);


console.log(found);