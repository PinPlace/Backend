const titleInput = document.querySelector('input[name=name]');
const slugInput = document.querySelector('input[name=slug]');

const slugify = (value) => {
    return value.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')  //replace and with -and-
        .replace(/[\s\W-]+/g, '-') //replaces spaces and non word chars and dsashed with a single dash
}

titleInput.addEventListener('keyup', (e)=>{
    slugInput.setAttribute('value', slugify(titleInput.value))
})
