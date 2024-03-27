//const tabs = document.querySelectorAll('[data-tab-target]')
//const tabContents = document.querySelectorAll('[data-tab-content]')

//tabs.forEach(tab => {
//    tab.addEventListener('click',() =>{
//        const target = document.querySelector(tab.dataset.tabTarget)
//        tabContents.forEach(tabContent => {
//            tabContent.classList.remove('active')
//        })
//        tabs.forEach(tab => {
//            tab.classList.remove('active')
//        })
//        tab.classList.add('active')
//        target.classList.add('active')
//    })
//})
document.getElementById('link1').addEventListener('click', function(){
    document.getElementById('about').classList.toggle('hidden');
    document.getElementById('home-content').classList.add('hidden');
});

document.getElementById('home-link').addEventListener('click', function(){
    document.getElementById('about').classList.add('hidden');
    document.getElementById('home-content').classList.remove('hidden');
});

function scrollToElement(elementSelector, instance = 0){
    const elements = document.querySelectorAll(elementSelector);
    if(elements.length > instance){
        elements[instance].scrollIntoView({behavior: 'smooth'});
    }
}

const link1 = document.getElementById("link1");
const link2 = document.getElementById("link2");

link1.addEventListener('click',() =>{
    scrollToElement('.header');
});

link2.addEventListener('click',() =>{
    scrollToElement('.header', 1);
});