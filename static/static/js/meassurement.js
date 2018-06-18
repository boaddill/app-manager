$(function () {

var loadForm = function () {


   
    
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      
      success: function (data) {
        $("#meassurements-container ").append(data.html_form);
      }
    });
  };
var createForm = function (){
$('form').each(  function(){
  
  var form = $(this);
  $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
         $("#meassurements-container ").html(data.html_meassurements);;
      
      }
    }
});
})
alert('Remenber to refresh scope main page to see the changes');
};

var deleteForm = function (){

var form = $(this);
  $.ajax({
      url: form.attr("data-url"),
      type: 'get',
      dataType: 'json',
      success: function (data) {

        
          
          $("#meassurements-container ").html(data.html_meassurements);
                
    }
});
};

// var deleteForm2 = function (){
// var btn = $(this);
//       $.ajax({
//       url: btn.attr("data-url"),
//       type: 'get',
//       dataType: 'json',
//       beforeSend: function () {
//         $("#modal-measurements").modal("show");
//       },
//       success: function (data) {
//         $(".modal-content").html(data.html_form);
//       }
//     });
// }

 var deleteAll = function() {

   $('[type=checkbox]').each(  function(){
    if ( $(this).is(':checked') ){

    var obj = $(this);
    $.ajax({
      url: obj.attr("data-url"),
      type: 'get',
      dataType: 'json',
      success: function (data) {
$("#meassurements-container ").html(data.html_meassurements);
    }
});

    
}
})

}
  $("#meassurements-load ").click(loadForm);
  $('.meassurements-submit').click(createForm);
  $("#meassurements-container ").on("click", ".meassurement-delete", deleteForm);
  $("body").on("click", ".delete-meassurements-selected", deleteAll);




})














