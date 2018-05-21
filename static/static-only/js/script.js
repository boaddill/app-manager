$(function (){

    $('#search_input').autocomplete({
        
        minLength: 2,
        source: function( req, add ) {
            var search=$('#search_input').val();
            $.ajax({
                dataType : 'json',
                method : 'GET',
                url : '/ajax/search/',
                data : { 'start':search, },
                success : function(data) {

                    
                    var suggestions = [];
                    $.each(data, function(index, objeto){
                        suggestions.push(objeto.value);
                        
                        
                    });
                    
                    add(suggestions);
                          
                },
                
                error:function(err){
                    alert('error');
                }
                          
            });                
        
        };
    
    }),
})












