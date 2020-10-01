const dropdownContainer = document.querySelector('.dropdown');

const zoomInOut = document.querySelector('.zoom-inout');

const switchContainer = document.querySelector('.switch-container');

const dropdownSocial = document.querySelector('.dropdown-social');

function myFunction() {
	dropdownContainer.classList.toggle('show');

	zoomInOut.style.display = 'none';

	switchContainer.style.display = 'none';

	dropdownSocial.style.display = 'inline';
}

function clearShare() {
	zoomInOut.style.display = 'inline';

	switchContainer.style.display = 'inline';

	dropdownSocial.style.display = 'none';
}

// document.querySelector('.dropbtn').addEventListener('click', function(e) {
// 	if (e.target !== document.querySelector('.dropbtn')) {
// 		console.log('You clicked outside');
// 	} else {
// 		console.log('You clicked inside');
// 	}
// });

// document.addEventListener('click', function(event) {

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

// Add the following code if you want the name of the file appear on select
// $('.custom-file-input').on('change', function() {
// 	var fileName = $(this).val().split('\\').pop();
// 	$(this).siblings('.custom-file-label').addClass('selected').html(fileName);
// });

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
