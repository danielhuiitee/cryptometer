$(document).ready(function() {


	var modal_button = document.getElementById("transaction-modal-btn");
	var modal = document.getElementById("transaction-modal");


	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("close-modal")[0];

	// When the user clicks on <span> (x), close the modal
	span.onclick = function() { 
	  modal.style.display = "none";
	}



	// if modal is open and clicked on then close it
	modal_button.onclick = function() {
		modal.style.display = "block";
	  
	}
});