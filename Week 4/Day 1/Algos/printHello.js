
function printHelloIterative( num ){
    let result = "";
    for ( let i = 0; i < num; i ++ ){
        result += "Hello ";
    }
    return result;
}

console.log( printHelloIterative( 10 ) );

function printHelloRecursive( num ){
    if( num === 1 ){
        return "Hello";
    }
    return "Hello " + printHelloRecursive( num - 1 );
}

console.log( printHelloRecursive( 5 ) );