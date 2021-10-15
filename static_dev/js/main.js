let menu_display = false
function open_menu(){
    let nav_menu = document.getElementById("nav-menu")
    let cat_menu = document.getElementById("cat-menu")
    let menu = document.getElementById("menu")

    if (menu_display){
        menu_display = false
        nav_menu.style.display = "none"
        if (cat_menu){
            cat_menu.style.top = menu.clientHeight + 'px'
        }
    }
    else {
        menu_display = true
        nav_menu.style.display = "flex"
        if (cat_menu){
            cat_menu.style.top = menu.clientHeight + 'px'
        }
    }
}