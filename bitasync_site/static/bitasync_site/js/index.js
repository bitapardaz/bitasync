

$(function() {
   
	 
	  $('#test').scrollToFixed();
	$('.res-nav_click').click(function(){
		$('.main-nav').slideToggle();
		return false    

	});
	
	 wow = new WOW(
      {
        animateClass: 'animated',
        offset:       100
      }
    );
    wow.init();
	
	
	
	$('.main-nav li a').bind('click',function(event){
				var $anchor = $(this);

				$('html, body').stop().animate({
					scrollTop: $($anchor.attr('href')).offset().top - 102
				}, 1500,'easeInOutExpo');
				/*
				if you don't want to use the easing effects:
				$('html, body').stop().animate({
					scrollTop: $($anchor.attr('href')).offset().top
				}, 1000);
				*/
				event.preventDefault();
			});


		var $container = $('.portfolioContainer'),
		  $body = $('body'),
		  colW = 375,
		  columns = null;

		 // modify Isotope's absolute position method
		$.Isotope.prototype._positionAbs = function( x, y ) {
		  return { right: x, top: y };
		};

	  $container.isotope({
		// disable window resizing
		 transformsEnabled: false,
		resizable: true,
		masonry: {
		  columnWidth: colW
		}
	  });

	  $(window).smartresize(function(){
		// check if columns has changed
		var currentColumns = Math.floor( ( $body.width() -30 ) / colW );
		if ( currentColumns !== columns ) {
		  // set new column count
		  columns = currentColumns;
		  // apply width to container manually, then trigger relayout
		  $container.width( columns * colW )
			.isotope('reLayout');
		}

	  }).smartresize(); // trigger resize to set container width


		$('.portfolioFilter a').click(function(){
			$('.portfolioFilter .current').removeClass('current');
			$(this).addClass('current');

			var selector = $(this).attr('data-filter');
			$container.isotope({

				filter: selector,
			 });
			 return false;
		});
	
	
});

	