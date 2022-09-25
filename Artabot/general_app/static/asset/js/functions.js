function isValid(element,errorElement,minLength = 0,message = "This field is reqired!"){
    if(element.value.trim().length <= minLength){
        errorElement.innerHTML = message
        element.style.border = "1px solid red"
        return false
    }else{
        errorElement.innerHTML = ""
        element.style.border = "1px solid green"
        return true
    }
}
const leftIcon = document.querySelector('.left-icon')
leftIcon.addEventListener('click',function (){
        window.location.replace('/')
});