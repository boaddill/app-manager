$(function () {
  /* Functions */
  var loadForm = function () {
   
    
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-chapter").modal("show");
      },
      success: function (data) {
        $(".modal-content").html(data.html_form);
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
          $("#project-container").html(data.html_scope);
          $("#modal-chapter").modal("hide");

      }
    }
});
    return false;
  };

  var pepe = function() {
    var url =$(this).attr("data-url");
    window.open(url, '', "width=1000,height=1000,scrollbars=yes");
    return false;

  };
  

  /* Binding */

  // Create chapter
  $(".chapter_create").click(loadForm);
  $("#modal-chapter").on("submit", ".js-chapter-create-form", saveForm);

  // Update chapter
  $("#project-container").on("click", ".js-update-chapter", loadForm);
  $("#modal-chapter").on("submit", ".js-chapter-update-form", saveForm);
    //delete chapter
  $("#project-container").on("click", ".js-delete-chapter", loadForm);
  $("#modal-chapter").on("submit", ".js-chapter-delete-form", saveForm);


  //call to measurement
  $("#project-container").on("click", ".meassurement_scope", pepe);
  $("#project-container").on("click", ".meassurement_real", pepe);

//////meassurements






})





