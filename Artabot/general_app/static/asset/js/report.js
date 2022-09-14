//Validate of Report form
const REmail = document.querySelector('.report_email')
const RText = document.querySelector('.report_text')
const RemailError = document.querySelector('.Remail_error')
const RtxtError = document.querySelector('.Rtxt_error')
const RSubmitBtn = document.querySelector('.report-btn')
RSubmitBtn.addEventListener('click',function (e){
    REmail_valid()
    RText_Valid()
    if(!REmail_valid()|| !RText_Valid()){
        e.preventDefault();
    }
})
REmail.addEventListener('keyup',()=>{
    REmail_valid()
})
RText.addEventListener('keyup',()=>{
    RText_Valid()
})

function REmail_valid(){
    if(REmail.value.trim().length <= 0){
        RemailError.innerHTML = "Please enter valid email"
        REmail.style.border = "1px solid red"
        return false
    }else{
        RemailError.innerHTML = ""
        REmail.style.border = "1px solid green"
        return true
    }
}

function RText_Valid(){
    if(RText.value.trim().length <= 10){
        RtxtError.innerHTML = "Report must has at least 10 characters"
        RText.style.border = "1px solid red"
        return false
    }else{
        RtxtError.innerHTML = ""
        RText.style.border = "1px solid green"
        return true
    }
}
const boldIcon = document.querySelector('.bold-icon')
boldIcon.onclick = ()=>{
    let boldTxt = document.querySelector('.report_text')
    boldTxt.select()
    document.execCommand('copy')
}