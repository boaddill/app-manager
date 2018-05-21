$("#pepe").mouseover(function () {
      var email = $('#id_email').val();

      $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'email': email
        },
        type: 'get',
        dataType: 'json',
        success: function (data) {
          if (email!=""){
          if (data.is_taken==false) {
            $("#pepe").prop('disabled', true);
            alert("A user with this username does not exists.");
            $("#pepe").prop('disabled', false);

          }
        }
            
        }
      
      });

    });