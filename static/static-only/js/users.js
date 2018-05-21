$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-book").modal("show");
      },
      success: function (data) {
        $(" .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#book-table tbody").html(data.html_user_list);
          $("#modal-book").modal("hide");

            if(data.action=='create'){


          $( "tr td:lt(5) " ).css( "background-color", "#FAB1FA" );

        };

        }




        else {


          $("#modal-book .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-book").click(loadForm);
  $("#modal-book").on("submit", ".js-book-create-form", saveForm);

  // Update book
  $("#book-table").on("click", ".js-update-book", loadForm);
  $("#modal-book").on("submit", ".js-book-update-form", saveForm);

  $("#book-table").on("click", ".js-delete-book", loadForm);
  $("#modal-book").on("submit", ".js-book-delete-form", saveForm);


  $("#buscador")
        .val('')
        .focus()
        .keyup(function () {

    var search =$("#buscador").val();
    $.ajax({
      url: '/user_filter_list',
      data: { 'q': search },
      type: 'get',
      dataType: 'json',
      success: function (data) {
        if (data) {
          $("#book-table tbody").html(data.html_user_list);
          $( ".pagination" ).remove();
          $( "td " ).addClass("table-success");


          
        }
        
      }
    });
    return false;

  
});




});

























