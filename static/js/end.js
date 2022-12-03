document.getElementById("btn_end").addEventListener("click", (e) => {
    const modal = document.getElementById("modal_container");
    modal.style.visibility = "visible";
    modal.style.opacity = 1;
});

document.addEventListener("click", (e) => {
    const modalContent = document.getElementById("modal");
    document.getElementById("sl").innerText =
        document.getElementById("number").innerText;
    const btn = document.getElementById("btn_end");
    document.getElementById("save").value =
        document.getElementById("number").innerText;

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
//count
document.getElementById("btn_count").addEventListener("click", (e) => {
    fetch(
        "http://henry102.click:5555/count",

        {
            method: "GET", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
        },
        (document.getElementById("animation").style.display = "flex")
    )
        .then((response) => {
            document.getElementById("animation").style.display = "none";
            return response.json();
        })

        .then((data) => {
            const span = document.getElementById("number");
            span.innerText = parseInt(span.innerText) + parseInt(data);
            window.alert("Số lượng đếm được: " + data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});

document.addEventListener("click", (e) => {
    const modalContent = document.getElementById("modal");
    const btn = document.getElementById("btn_count");

    if (!modalContent.contains(e.target) && !btn.contains(e.target)) {
        const modal = document.getElementById("modal_container_count");
        modal.style.visibility = "hidden";
        modal.style.opacity = 0;
    }
});

// document.getElementById("confirm_form").addEventListener("submit", (e) => {
//     e.preventDefault();
// });
