/**
 * Applies a temporary transition effect to the sidebar.
 *
 * @function applySidebarTransition
 * @returns {void}
 */
function applySidebarTransition() {
  const sidebar = document.getElementById("sidebar");

  sidebar.style.transition = "width 0.25s ease";

  setTimeout(() => {
    sidebar.style.transition = "";
  }, 250);
}
