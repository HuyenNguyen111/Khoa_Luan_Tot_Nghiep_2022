document.getElementById("btn_end").addEventListener("click", (e) => {
    const modal = document.getElementById("modal_container");
    modal.style.visibility = "visible";
    modal.style.opacity = 1;
});

document.addEventListener("click", (e) => {
    const modalContent = document.getElementById("modal");
    const btn = document.getElementById("btn_end");

    if (!modalContent.contains(e.target) && !btn.contains(e.target)) {
        const modal = document.getElementById("modal_container");
        modal.style.visibility = "hidden";
        modal.style.opacity = 0;
    }
});

document.getElementById("close_modal").addEventListener("click", (e) => {
    const modal = document.getElementById("modal_container");
    modal.style.visibility = "hidden";
    modal.style.opacity = 0;
});

// document.getElementById("confirm_form").addEventListener("submit", (e) => {
//     e.preventDefault();
// });
