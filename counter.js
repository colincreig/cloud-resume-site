document.addEventListener("DOMContentLoaded", () => {
  let count = localStorage.getItem("visitCount") || 0;
  count++;
  localStorage.setItem("visitCount", count);
  document.getElementById("visitor-count").textContent = count;
});