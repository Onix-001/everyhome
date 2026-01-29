document.getElementById("sidebarToggle").addEventListener("click", function () {
  document.querySelector(".sidebar").classList.toggle("collapsed");
  document.querySelector(".main-panel").classList.toggle("collapsed");
});







/* SCRIPT GESUSER */

document.addEventListener("DOMContentLoaded", function () {

  const toggleBtn = document.getElementById("sidebarToggle");
  const sidebar = document.querySelector(".sidebar");
  const colLg12GridMargin = document.querySelector(".col-lg-12.grid-margin.stretch-card");

  if (!toggleBtn || !sidebar || !colLg12GridMargin) {
    console.error("Sidebar toggle elements not found");
    return;
  }

  toggleBtn.addEventListener("click", function () {
    sidebar.classList.toggle("collapsed");
    colLg12GridMargin.classList.toggle("collapsed");
    const icon = toggleBtn.querySelector("i");
    icon.classList.toggle("mdi-menu");
    icon.classList.toggle("mdi-menu-open");
  });

});