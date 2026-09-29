//Primitive Types
let myString: string = "test"
let myNumber: number = 21
let myBoolean: boolean = true

//Arrays
let numberArray: number[] = [5,6,7]
let stringArray: string[] = ["test"]
let genericArray: Array<string> = ["test"] //just another way to write the same thing

//Any
let obj: any = [5,6]
obj.foo() //no compilation error even though foo doesnt exist because of any
obj = 'hello' //can be reassigned to anything

//Functions
function greet(name: string){
    console.log("Hello" + name)
}

function adding(a: number, b:number): number{ //return types can be explicit but not necessary or needed
    return a+b
}

//Objects
function printCoord(pt: {x?: number, y:number}){ //? means that its optional
    if (obj.x == undefined){ //need to check if its there  or not
        console.log(obj.y)
    }
    else{
        console.log("The coordinate's x value is " + pt.x);
        console.log("The coordinate's y value is " + pt.y);
    }
}

//Union types
function testUnion(id: string | number){
    // Narrowing: TypeScript deduces the specific type in a code block.
    if (typeof id === "string"){
        console.log(id.toUpperCase)
    }
    else{
        console.log(id)
    }
}

//Type Aliases
type pointAlias = {x: number, y: number}
function adder(p: pointAlias){
    return p.x + p.y
}

//Interfaces vs types
interface Animal {name: string}
interface bear extends Animal {honey: boolean}

type Animaltype = {name: string}
type Beartype = Animaltype & {honey: boolean}

//Interfaces support "Declaration Merging" (re-opening an interface to add fields), types can't
interface Window { title: string; }
interface Window { ts: string; }

//Literal types
function printText(s: string, a: "left" |"right"){
    console.log(s + a)
}
printText("Hello, world", "left");
// printText("Hello", "bottom"); // Error: "bottom" is not assignable

//Type Assertions
// req1.method is inferred as 'string', not the literal '"GET"'.
const req1 = { url: "https://example.com", method: "GET" };
// To fix this, use a type assertion on the property...
const req2 = { url: "https://example.com", method: "GET" as "GET" };



