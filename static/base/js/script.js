function ConvertNavBar(){
    let visible = document.getElementsByClassName("collapse show");
    let hidden = document.getElementsByClassName("collapse");
    let activator = document.getElementsByClassName("navbar-toggler");

    if (visible = true) {
        activator(onclick="visible.classList.replace('collapse show', 'collapse');")
        console.log("visible");
    }

    else if (hidden = true){
        activator(onclick="visible.classList.replace('collapse', 'collapse show');")
        console.log("hidden");
    }

    else {
        console.log("Error! invalide class name")
    }

}