//Scroll Shadow
window.addEventListener('scroll',()=>{
    const navTop = document.getElementById('nav-top');
    if(scrollY > 1){
        navTop.classList.add('scroll');
    }
    else{
        navTop.classList.remove('scroll');
    }
})
// Toggle Dark and Light mode
const body = document.body
const toggleMode = document.querySelector('.theme-icon')
const darkIcon = document.querySelector('.dark-icon')
const lightIcon = document.querySelector('.light-icon')

if(toggleMode){
    toggleMode.addEventListener('click',function (){
        body.classList.toggle('dark')
        darkIcon.classList.toggle('active')
        lightIcon.classList.toggle('active')
        
        if(body.classList.contains('dark')){
            localStorage.setItem('mode','dark')
        }
        else{
            localStorage.setItem('mode','light')
        }
    });
}

if(localStorage.getItem('mode') == 'dark'){
    const body = document.body
    body.classList.toggle('dark')
}

const menuLink = document.querySelectorAll('.menu-link')
menuLink.forEach(link =>{
    if(link.href == location.href){
        link.classList.add('current-page')
    }
});

// Language Page
const Languages = document.querySelectorAll('.language')
Languages.forEach(Language =>{
    if(Language.href == location.href){
        Language.classList.add('current-page')
    }
});

// Search and Back Button for mobile
const searchBtn = document.querySelector('.search-icon')
const backBtn = document.querySelector('.back-icon')
const searchBox = document.querySelector('.search-box')

searchBtn.addEventListener('click',function (){
    searchBox.classList.add("opened")
});
backBtn.addEventListener('click',function (){
    searchBox.classList.remove("opened")
});

// Menu-side-bar
const MenuBtn = document.querySelector('.menu-icon')
const Scrim = document.querySelector('.scrim')
const NavSide = document.querySelector('.nav-side')
const NavSideBar = document.querySelector('.nav-side-bar')
const CancelBtn = document.querySelector('.cancel-btn')

MenuBtn.addEventListener('click',function (){
    NavSide.classList.toggle("opened")
    NavSideBar.classList.toggle("opened")
});
Scrim.addEventListener('click',function (){
    NavSide.classList.remove("opened")
    NavSideBar.classList.remove("opened")
});
CancelBtn.addEventListener('click',function (){
    NavSide.classList.remove("opened")
    NavSideBar.classList.remove("opened")
});

//search box query
const searchQuery = document.getElementById('search-query')
const searchLists = document.querySelector('.search-lists')
const searchList = document.querySelectorAll('.search-list')
const searchSubmitBtn = document.querySelector('.search-submit-icon')

searchSubmitBtn.addEventListener('click',(event)=>{
    if (searchQuery.value.trim().length <= 0){
        event.preventDefault()
    }
})