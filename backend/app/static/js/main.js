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
