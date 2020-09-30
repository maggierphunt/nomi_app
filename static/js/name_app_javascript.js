const dropdown = document.querySelector('.dropdown');
const zoomInOut = document.querySelector('.zoom-inout');
const switchContainer = document.querySelector('.switch-container');
const dropdownSocial = document.querySelector('.dropdown-social');

function myFunction() {
	dropdown.classList.toggle('show');

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

console.log('hello');
