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


// Custom cursor
document.addEventListener("DOMContentLoaded", () => {
  const cursor = document.getElementById("custom-cursor");

  let mouseX = 0;
  let mouseY = 0;
  let currentX = 0;
  let currentY = 0;
  const speed = 0.4;

  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
  });

  function animate() {
    currentX += (mouseX - currentX) * speed;
    currentY += (mouseY - currentY) * speed;

    // 👇 Apply clean left/top and single transform
    cursor.style.left = `${currentX}px`;
    cursor.style.top = `${currentY}px`;
    cursor.style.transform = `translate(-50%, -50%)`;

    requestAnimationFrame(animate);
  }

  animate();

  // Hover effect
  const interactive = document.querySelectorAll("a, button, .button");

  interactive.forEach((el) => {
    el.addEventListener("mouseenter", () => {
      cursor.style.width = "40px";
      cursor.style.height = "40px";
    });
    el.addEventListener("mouseleave", () => {
      cursor.style.width = "20px";
      cursor.style.height = "20px";
    });
  });
});
