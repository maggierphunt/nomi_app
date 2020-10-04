// Recording

const dropdownSocial = document.querySelector('.dropdown-social');

var recording = document.getElementById('recording');

var recordedAudio = document.getElementById('recordedAudio');

var recordedAudio2 = document.getElementById('recordedAudio2');

var firstNameRec = document.getElementById('NameRecording');

var replay = document.getElementById('replay');

const stylesOn = {
	border: 'none',
	color: 'white',
	boxShadow: 'none',
	backgroundColor: 'salmon'
};

const stylesOff = {
	border: '1px solid salmon',
	color: 'salmon',
	boxShadow: 'none',
	backgroundColor: 'white'
};

// Dark Mode Toggle

function darkmodeToggle() {
	const body = document.body;
	body.classList.toggle('dark-mode');

	// const header = document.querySelector('.header-container');
	// header.classList.toggle('dark-mode2');

	// const footer = document.querySelector('.footer-container');
	// footer.classList.toggle('dark-mode2');
}

// Image Upload

const customFileInput = document.querySelector('#FirstNameImage');
const customFileLabel = document.querySelector('#FirstNameLabel');
const lastNameInput = document.querySelector('#LastNameImage');
const lastNameLabel = document.querySelector('#LastNameLabel');

customFileInput.addEventListener('change', function() {
	const fileName = customFileInput.value.split(/[\\\/]/).pop();
	customFileLabel.innerHTML = fileName;
});

lastNameInput.addEventListener('change', function() {
	const fileName = lastNameInput.value.split(/[\\\/]/).pop();
	lastNameLabel.innerHTML = fileName;
});

// Image Upload - Error Messages

const firstNameErrorMessage = document.querySelector('.first-name-error');
const lastNameErrorMessage = document.querySelector('.last-name-error');

function validateFirstName(file) {
	var fileSize = file.files[0].size / 1024 / 1024; // in MB
	if (fileSize > 2) {
		// alert('File size exceeds 2 MB');
		firstNameErrorMessage.style.display = 'block';
		firstNameErrorMessage.innerHTML =
			'File size exceeds 2 MB please upload a smaller file';
	} else {
		firstNameErrorMessage.style.display = 'none';
	}
}

function validateLastName(file) {
	var fileSize = file.files[0].size / 1024 / 1024; // in MB
	if (fileSize > 2) {
		// alert('File size exceeds 2 MB');
		lastNameErrorMessage.style.display = 'block';
		lastNameErrorMessage.innerHTML =
			'File size exceeds 2 MB please upload a smaller file';
	} else {
		lastNameErrorMessage.style.display = 'none';
	}
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

// Recording

navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
	handlerFunction(stream);
});

function handlerFunction(stream) {
	rec = new MediaRecorder(stream);
	rec.ondataavailable = (e) => {
		audioChunks.push(e.data);
		if (rec.state == 'inactive') {
			let blob = new Blob(audioChunks, { type: 'audio/ogg' });
			const url = URL.createObjectURL(blob);
			recordedAudio.src = url;
			var xhr = new XMLHttpRequest();
			xhr.open('POST', url, true);
			xhr.responseType = 'blob';
			firstNameRec.value = url;
			//                recordingLink.href = url;
			//                rec.download = 'audio/ogg';
		}
	};
}

function startR(e) {
	if (
		recording.innerHTML == 'Start Recording' ||
		recording.innerHTML == 'Retry'
	) {
		audioChunks = [];
		rec.start();
		recording.innerHTML = 'Stop Recording';
		Object.assign(recording.style, stylesOn);
		recording.style.width = '100%';
		replay.style.visibility = 'hidden';
	} else {
		rec.stop();
		recording.innerHTML = 'Retry';
		Object.assign(recording.style, stylesOff);
		recording.style.width = '60%';
		replay.style.visibility = 'visible';
	}
}

function play() {
	recordedAudio.play();
}
function playAudio() {
	recordedAudio2.play();
}
