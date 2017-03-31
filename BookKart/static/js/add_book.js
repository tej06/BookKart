$(function(){
	$('#btnadd').click(function(){
		
		$.ajax({
			url: '/add_success',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
