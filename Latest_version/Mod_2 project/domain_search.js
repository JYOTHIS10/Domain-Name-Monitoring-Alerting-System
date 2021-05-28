// domain search bar

//user page

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  links.forEach(link => {
    link.classList.toggle("fade");
  });
});

$(document).ready(function() {
	$('.hamburger').click(function() {
		$('.content').fadeToggle()
	});

	$('.hamburger').click(function() {
		$('.content').delay(3000).slideIn(5000)
	});
});

