const dropdownContainer = document.querySelector('#myDropdown');
const zoomInOut = document.querySelector('.zoom-inout');
const switchContainer = document.querySelector('.switch-container');

// const myFunction = () => {
// 	dropdownContainer.classList.toggle('show');
// 	zoomInOut.style.display = 'none';
// 	switchContainer.style.display = 'none';
// 	dropdownSocial.style.display = 'inline';
// };

// function clearShare() {
// 	zoomInOut.style.display = 'inline';
// 	switchContainer.style.display = 'inline';
// 	dropdownSocial.style.display = 'none';
// }

// const shareBtn = document.querySelector('.sharebtn');

// shareBtn.addEventListener('click', function() {
// 	dropdownContainer.classList.toggle('show');
// 	zoomInOut.style.display = 'none';
// 	switchContainer.style.display = 'none';
// 	dropdownSocial.style.display = 'inline';
// });

// Dark Mode Toggle

function darkmodeToggle() {
	const body = document.body;
	body.classList.toggle('dark-mode');

	const header = document.querySelector('.header-container');
	header.classList.toggle('dark-mode2');

	const footer = document.querySelector('.footer-container');
	footer.classList.toggle('dark-mode2');
}

// Image Upload

const customFileInput = document.querySelector('.custom-file-input');
const customFileLabel = document.querySelector('.custom-file-label');

const customRecording = document.querySelector('.recording');
const customRecordingLabel = document.querySelector('.recording-label');

customFileInput.addEventListener('change', function() {
	const fileName = customFileInput.value.split(/[\\\/]/).pop();
	customFileLabel.innerHTML = fileName;
});

customRecording.addEventListener('change', function() {
	const recordingFileName = customRecording.value.split(/[\\\/]/).pop();
	customRecordingLabel.innerHTML = recordingFileName;
});

// Show/hide social icons

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
		switchContainer.style.display = 'inline';
	}
});

let showSocials = false;
