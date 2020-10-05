// Dark Mode Toggle

function darkmodeToggle() {
	const body = document.body;
	body.classList.toggle('dark-mode');

	// const header = document.querySelector('.header-container');
	// header.classList.toggle('dark-mode2');

	// const footer = document.querySelector('.footer-container');
	// footer.classList.toggle('dark-mode2');
}

// Show/hide social icons

const zoomInOut = document.querySelector('.zoom-inout');
const switchContainer = document.querySelector('.switch-container');

document.querySelector('.sharebtn').addEventListener('click', function() {
	const footerNav = document.querySelector('.footer-navbar');

	showSocials = !showSocials;

	if (showSocials === true) {
		footerNav.style.display = 'inline-flex';
		zoomInOut.style.display = 'none';
		switchContainer.style.display = 'none';
	} else {
		footerNav.style.display = 'none';
		zoomInOut.style.display = 'inline';
		switchContainer.style.display = 'flex';
	}
});

let showSocials = false;