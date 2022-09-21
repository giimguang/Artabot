//Validate of Report form
const reportEmail = document.querySelector('.report_email')
const reportEmailError = document.querySelector('.report_email_error')

const reportDetail = document.querySelector('.report_detial')
const reportDetailError = document.querySelector('.report_detial_error')

const reportSubmitBtn = document.querySelector('.report-btn')

reportSubmitBtn.addEventListener('click',function (e){
    let reportEmailValid = isValid(reportEmail,reportEmailError,0,"Please enter valid email")
    let reportDetailValid = isValid(reportDetail,reportDetailError,10,'Report must has at least 10 characters')
    if(!reportEmailValid|| !reportDetailValid){
        e.preventDefault();
    }
})

reportEmail.addEventListener('keyup',()=>{
    isValid(reportEmail,reportEmailError,0,"Please enter valid email")
})
reportDetail.addEventListener('keyup',()=>{
    isValid(reportDetail,reportDetailError,10,'Report must has at least 10 characters')
})