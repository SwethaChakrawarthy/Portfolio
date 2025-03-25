const navItems = document.querySelectorAll("nav ul li");
const tracker = document.querySelector(".nav-tracker");

function moveTrackerTo(el) {
  const rect = el.getBoundingClientRect();
  const parentRect = el.parentElement.getBoundingClientRect();
  tracker.style.width = `${rect.width}px`;
  tracker.style.transform = `translateX(${rect.left - parentRect.left}px)`;
}

navItems.forEach((li) => {
  li.addEventListener("click", () => {
    document.querySelector("nav ul li.active")?.classList.remove("active");
    li.classList.add("active");
    moveTrackerTo(li);
  });
});

window.addEventListener("DOMContentLoaded", () => {
  const active = document.querySelector("nav ul li.active");
  if (active) moveTrackerTo(active);
});
