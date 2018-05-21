$("#id_email").change(function () {
      var dat = $(this).val();

      $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'email': dat
        },
        type: 'get',
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists , please choose another one");
            // $("#id_password1").prop('disabled', true);
            // $("#id_password2").prop('disabled', true);
            // $("#id_is_active").prop('disabled', true);
            // $("#id_user_type").prop('disabled', true);
            $("#pepe1").prop('disabled', true);

          }
          else{
            // $("#id_password1").prop('disabled', false);
            // $("#id_password2").prop('disabled', false);
            // $("#id_is_active").prop('disabled', false);
            // $("#id_user_type").prop('disabled', false);
            $("#pepe1").prop('disabled', false);
          }
        }
      });

    });