

$(function() {
   
   $('.linkscroll').click(function()
   { 
	
		
		$('html, body').stop().animate({
				scrollTop: $( $(this).attr('href') ).offset().top - 30
			}, 800);
			
	});
	
	
  
$(window).resize(function() {
    
	
	//$('#hero').height($(window).height()-$('#test').height());
	//alert($('#hero').height());
	if($('#hero').height()<$(window).height())
		$('#hero').height($(window).height());
	//alert($(window).height());


}).resize();
	
	
});

	