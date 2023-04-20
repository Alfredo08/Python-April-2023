async function loadTodos( element ){
    let URL = "http://127.0.0.1:5000/api/todos";
    let settings = {
        method : "GET"
    }

    let response = await fetch( URL, settings );
    let data = await response.json();

    let listTodos = document.querySelector( ".todos" );
    listTodos.innerHTML = "";
    for( let i = 0; i < data.length; i ++ ){
        listTodos.innerHTML += `
            <li>
                ${data[i].status} - ${data[i].name}
            </li>
        `;
    }
}

async function addNewTodo(event){
    event.preventDefault();

    let URL = "http://127.0.0.1:5000/api/new/todo";
    let new_todo = {
        "name" : document.querySelector( "#name" ).value,
        "status" : document.querySelector( "#status" ).value,
        "user_id" : document.querySelector( "#user_id" ).value
    };
    console.log( new_todo );
    let settings = {
        method : "POST",
        headers : {
            "Content-type" : "application/json"
        },
        body : JSON.stringify( new_todo )
    };
    let response = await fetch( URL, settings );
    // DO NOT EXECUTE THIS LINE ON A DELETE!
    let data = await response.json();
    
    if ( response.status === 406 ){
        document.querySelector( ".errorMessage" ).innerText = data.message
    }
    else{
        let listTodos = document.querySelector( ".todos" );
        listTodos.innerHTML += `
            <li>
                ${new_todo.status} - ${new_todo.name}
            </li>
        `;
        document.querySelector( ".errorMessage" ).innerText = "";
    }
}