// the Back link returns to the page that opened this one, when there is one; in the extension, Fude's page is panel.html
const back=document.getElementById('back'),ext=location.protocol==='chrome-extension:';
if(ext)back.href='panel.html';
back.addEventListener('click',e=>{if(history.length>1&&(document.referrer||ext)){e.preventDefault();history.back()}})
