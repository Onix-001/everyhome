document.addEventListener("DOMContentLoaded", function () {

    const toggleBtn = document.getElementById("sidebarToggle");
    const sidebar = document.querySelector(".sidebar");
    const stretchCard = document.querySelector(".stretch-card");

    if (!toggleBtn || !sidebar || !card) {
        console.error("Sidebar toggle elements not found");
        return;
    }

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("collapsed");
        card.classList.toggle("collapsed");

        const icon = toggleBtn.querySelector("i");
        icon.classList.toggle("mdi-menu");
        icon.classList.toggle("mdi-menu-open");
    });

});