function ocultagoUp() {
    document.querySelector(".goUp").classList.add("goUp--is-hidden")
}
function exibegoUp() {
    document.querySelector(".goUp").classList.remove("goUp--is-hidden")
}
document.addEventListener("DOMContentLoaded", (function () {
    AOS.init();
    const e = document.getElementById("menu")
        , o = e.clientHeight;
    window.addEventListener("scroll", (function () {
        window.scrollY < o - 100 ? ocultagoUp() : exibegoUp()
    }
    )),
        Array.from(document.getElementsByClassName("menu__items__item")).forEach(((o, t) => {
            o.onmouseover = () => {
                e.dataset.activeIndex = t
            }
        }
        ))
}
));