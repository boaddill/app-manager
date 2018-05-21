$("#id_email").change(function () {
      var email = $(this).val();

      $.ajax({
        url: '/ajax/validate_username/',
        data: {
          'email': email
        },
        type: 'get',
        dataType: 'json',
        success: function (data) {
          if (data.is_taken) {
            alert("A user with this username already exists , please choose another one");
            $("#id_password1").prop('disabled', true);
          }
          else{
            $("#id_password1").prop('disabled', false);
          }
        }
      });

    });