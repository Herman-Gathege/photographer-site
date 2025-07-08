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
