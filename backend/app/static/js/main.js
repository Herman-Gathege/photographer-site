// Easter egg: Type "adm" to go to login page
let typedKeys = [];

window.addEventListener('keydown', function (e) {
  typedKeys.push(e.key.toLowerCase());

  // Only keep the last 10 keystrokes
  if (typedKeys.length > 10) typedKeys.shift();

  if (typedKeys.join('').includes('adm')) {
    window.location.href = "/auth/login"; // Update if your login route is different
  }
});


// Dropdown functionality
// This code handles dropdown menus in the admin panel
// It toggles the visibility of the dropdown menu when the toggle button is clicked
// and hides the menu when clicking outside of it.
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function (e) {
      const menu = this.nextElementSibling;
      menu.classList.toggle('hidden');

      // Optional: hide others
      document.querySelectorAll('.dropdown-menu').forEach(m => {
        if (m !== menu) m.classList.add('hidden');
      });

      // Close on outside click
      document.addEventListener('click', function outsideClickListener(ev) {
        if (!menu.contains(ev.target) && ev.target !== toggle) {
          menu.classList.add('hidden');
          document.removeEventListener('click', outsideClickListener);
        }
      });
    });
  });
});


// Gallery modal functionality
// This code handles the image gallery modal functionality
// It opens a modal with a larger view of the clicked image and allows zooming in/out
// It also closes the modal when clicking outside the image or pressing Escape.
// It uses the "hidden" class to show/hide the modal.
document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("galleryModal");
  const modalImg = document.getElementById("modalImage");
  const closeBtn = document.querySelector(".close-modal");

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

  // Optional: close on Escape
  window.addEventListener("keydown", e => {
    if (e.key === "Escape") {
      modal.classList.add("hidden");
      modal.classList.remove("zoom");
      modalImg.src = "";
    }
  });
});
