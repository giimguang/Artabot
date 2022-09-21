const textEditor = document.getElementById('text_editor');
const toolBtn = document.querySelectorAll('.tool--btn');

toolBtn.forEach(btn =>{
    btn.addEventListener('click', () => {
        textEditor.focus()
        let cmd = btn.dataset['command'];
        if(cmd === 'createlink' || cmd === 'insertImage') {
            let url = prompt("Enter the link here: ");
            if(url != ""){
                document.execCommand(cmd, false, url);
            }
        } else if(cmd === 'code'){
            document.execCommand(cmd, false, div);
        }
         else {
            document.execCommand(cmd, false, null);
        }
    })
})

const form = document.getElementById('editor-form')

form.onsubmit = () => {
    let textContent = document.getElementById('text_content')
    textContent.innerHTML = textEditor.innerHTML
}

//Check validation of form
const title = document.querySelector('.title')
const titleErr = document.querySelector('.title-err')

const editorTag = document.querySelector('.editor-tag')
const editorTagErr = document.querySelector('.editor-tag-err')

const editorLang = document.querySelector('.editor-lang')

const submitBtn = document.querySelector('#editor-submit')
submitBtn.addEventListener('click',function (e){
    let titleValid = isValid(title,titleErr,0,"Title is required!")
    let editorTagValid = isValid(editorTag,editorTagErr,0,"Tag is required!")
    if(!titleValid || !editorTagValid){
        e.preventDefault();
    }
})

//Hide and show password
const showIcon = document.querySelector('.show-icon')
const PasswordType = document.querySelector('.password')

showIcon.addEventListener('click',()=>{
    if(PasswordType.type === "text"){
        PasswordType.setAttribute('type', 'password')
        showIcon.innerHTML = '<path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/><path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>'
    }else{
        PasswordType.setAttribute('type', 'text')
        showIcon.innerHTML = '<path d="M13.359 11.238C15.06 9.72 16 8 16 8s-3-5.5-8-5.5a7.028 7.028 0 0 0-2.79.588l.77.771A5.944 5.944 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755-.165.165-.337.328-.517.486l.708.709z"/><path d="M11.297 9.176a3.5 3.5 0 0 0-4.474-4.474l.823.823a2.5 2.5 0 0 1 2.829 2.829l.822.822zm-2.943 1.299.822.822a3.5 3.5 0 0 1-4.474-4.474l.823.823a2.5 2.5 0 0 0 2.829 2.829z"/><path d="M3.35 5.47c-.18.16-.353.322-.518.487A13.134 13.134 0 0 0 1.172 8l.195.288c.335.48.83 1.12 1.465 1.755C4.121 11.332 5.881 12.5 8 12.5c.716 0 1.39-.133 2.02-.36l.77.772A7.029 7.029 0 0 1 8 13.5C3 13.5 0 8 0 8s.939-1.721 2.641-3.238l.708.709zm10.296 8.884-12-12 .708-.708 12 12-.708.708z"/>'
    }
})