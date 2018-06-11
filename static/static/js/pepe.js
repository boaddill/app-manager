$(document).ready(function(){

	$("#real").click(function(){
    $(".real").toggle();
});	
	$("#planif").click(function(){
    $(".planif").toggle();

})

	$("#scope").click(function(){
    $(".scope").toggle();

})
	$("#invoice").click(function(){
    $(".invoice").toggle();

})
	$("#target").click(function(){
    $(".target").toggle();
})	


	var toggle = function(){
		var pepe=$(this).attr('id');
	 	$("."+pepe).toggle();

	 	// $('tr.main').not($(this).parent()).toggle();
	 	$('.entry-item').hide();

// class='{{entry.id}} 


	}

	var toggle2 = function(){
		var pepe1=$(this).attr('id');
	 	$("tr."+pepe1).toggle();

	}




$("#project-container").on("click", ".entry", toggle);
$('#project-container').on('click','.item',toggle2);


  
	   

	    

	  	
	})
	

	
		
	
