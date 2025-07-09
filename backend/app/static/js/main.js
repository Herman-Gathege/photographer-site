// Easter egg: Type "adm" to go to login page
let typedKeys = [];

window.addEventListener('keydown', function (e) {
  typedKeys.push(e.key.toLowerCase());

  if (typedKeys.length > 10) typedKeys.shift();

  if (typedKeys.join('').includes('adm')) {
    window.location.href = "/auth/login"; // Adjust as needed
  }
});

// Dropdown functionality
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function () {
      const menu = this.nextElementSibling;
      if (!menu) return;

      menu.classList.toggle('hidden');

      document.querySelectorAll('.dropdown-menu').forEach(m => {
        if (m !== menu) m.classList.add('hidden');
      });

      // Close on outside click
      const outsideClickListener = (ev) => {
        if (!menu.contains(ev.target) && ev.target !== toggle) {
          menu.classList.add('hidden');
          document.removeEventListener('click', outsideClickListener);
        }
      };

      document.addEventListener('click', outsideClickListener);
    });
  });
});

// Gallery modal functionality
document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("galleryModal");
  const modalImg = document.getElementById("modalImage");
  const closeBtn = document.querySelector(".close-modal");

  // Only run if the modal elements exist on the page
  if (modal && modalImg && closeBtn) {
    document.querySelectorAll(".gallery-image").forEach(img => {
      img.addEventListener("click", () => {
        modal.classList.remove("hidden");
        modal.classList.remove("zoom");
        modalImg.src = img.dataset.src;
      });
    });

    closeBtn.addEventListener("click", () => {
      modal.classList.add("hidden");
      modalImg.src = "";
    });

    modalImg.addEventListener("click", () => {
      modal.classList.toggle("zoom");
    });

    window.addEventListener("keydown", e => {
      if (e.key === "Escape") {
        modal.classList.add("hidden");
        modal.classList.remove("zoom");
        modalImg.src = "";
      }
    });
  }
});

// Hamburger menu functionality
document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.getElementById("hamburgerBtn");
  const navContainer = document.querySelector(".nav-container");

  if (hamburger && navContainer) {
    hamburger.addEventListener("click", () => {
      navContainer.classList.toggle("show");
    });
  }
});
