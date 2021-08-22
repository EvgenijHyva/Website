let isDark = JSON.parse(localStorage.getItem("Dark")) || false;

document.documentElement.setAttribute("data-theme", isDark ? "dark" : "light")