document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".back-top").forEach(btn => {
    btn.addEventListener("click", e => {
      e.preventDefault();
      window.scrollTo({top: 0, behavior: "smooth"});
    });
  });
});
