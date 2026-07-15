async function loadNotes(){

    let response = await fetch('/notes');

    let notes = await response.json();

    let list = document.getElementById("notesList");

    list.innerHTML = "";

    notes.forEach(note => {

        let li = document.createElement("li");

        li.innerText = note.content;

        list.appendChild(li);

    });

}

async function saveNote(){

    let note = document.getElementById("note").value;

    if(note==""){

        alert("Please enter a note");

        return;

    }

    await fetch('/notes',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            content:note
        })

    });

    document.getElementById("note").value="";

    loadNotes();

}

loadNotes();