
jQuery(document).ready(function() {
	

    /*
        Form validation
    */
    $('.registration-form input[type="text"], .registration-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    $('.registration-form').on('submit', function(e) {
    	
    			
		
		
	//	if($('.input1').length > 0 && $('input1').val() != '')
		if( $('#id_user-username').val() == "" ) 
			{
					
				
					e.preventDefault();
					$('#id_user-username').addClass('input-error');
			}
    	else
			{
					
				$(this).removeClass('input-error');
			}
		
		if( $('#id_user-password1').val() == "" ) 
			{
					e.preventDefault();
					$('#id_user-password1').addClass('input-error');
			}
    	else
			{
					$(this).removeClass('input-error');
			}
		
		if( $('#id_user-password2').val() == "" ) 
			{
					e.preventDefault();
					$('#id_user-password2').addClass('input-error');
			}
    	else
			{
					$(this).removeClass('input-error');
			}
		
		if( $('#id_userprofile-email').val() == "" ) 
			{
					e.preventDefault();
					$('#id_userprofile-email').addClass('input-error');
			}
    	else
			{
					$('#id_userprofile-email').removeClass('input-error');
			}
		
		if( $('#id_userprofile-read_agreement').is(':checked') ) 
			{
					
				
					
			}
    	else
			{
				
				alert("لطفا شرایط موافقت نامه را بخوانید");	
				e.preventDefault();
				
			}
		
		
		
		
		/*$(this).find('input[type="text"], textarea').each(function()
		{
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});*/
    	
    
	
	
	
	});
    
    
});
