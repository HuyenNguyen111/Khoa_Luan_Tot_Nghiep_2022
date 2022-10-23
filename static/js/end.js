document.getElementById("my_form").addEventListener("submit", (e) => {
    e.preventDefault();
    const modal = document.getElementById("modal_container");
    modal.style.visibility = "visible";
    modal.style.opacity = 1;
});

document.addEventListener("click", (e) => {
    const modalContent = document.getElementById("modal");
    if (!modalContent.contains(e.target)) {
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
