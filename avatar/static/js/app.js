const toggleBtn = document.getElementById('themeToggle');
const body = document.body;
const icon = toggleBtn.querySelector('i');

// Aplica o tema salvo no localStorage
if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-mode');
    icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
}

toggleBtn.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    const isDark = body.classList.contains('dark-mode');
    icon.classList.replace(isDark ? 'bi-moon-fill' : 'bi-sun-fill', isDark ? 'bi-sun-fill' : 'bi-moon-fill');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});