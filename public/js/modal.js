$(document).ready(function() {


	var modal_button = document.getElementById("transaction-modal-btn");
	var modal = document.getElementById("transaction-modal");
	var submitFormBtn = document.getElementById("submitForm");


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




	$("#transaction-form").submit(function(e) {

        e.preventDefault();

        //do your own request an handle the results
 		$.ajax({
		    url: e.currentTarget.action,
		    type: 'post',
            dataType: 'json',
            data: $("#transaction-form").serialize(),
		    success: function (data) {
		        console.log(data["stats"]);  
		        console.log(data["historicalData"]);    

		        var stats = data["stats"];
		        var historicalData = data["historicalData"];
		    },
		    error: function (data) {
		    	console.log("error")
		    	console.log(data);     
		    	window.alert("Error with transaction " + data);

		    }
		});

    });


	function loadHistoricalData(){

	}

	function loadCryptoStats(){

	}

});