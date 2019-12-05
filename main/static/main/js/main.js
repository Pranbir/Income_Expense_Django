
function activateSidebar(){
    let pageName = window.location.pathname; // Get URL PATH
    $('.nav > .nav-item').removeClass("active"); // Remove active class from all item if available
    $('.nav > .nav-item').each(function(){ // Check all nav item
        if($(this).find('a').attr('href') && $(this).find('a').attr('href') == pageName){ // If nav item is maching with the path, Add the active class
            $(this).addClass("active");
            return false;
        }
     });
}


$(document).ready( function(){
    
    activateSidebar();
    
});