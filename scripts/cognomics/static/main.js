$(function() {
  $('#approveBtn').bind('click', function() {
    $.getJSON('/_approve_btn_pressed', {

    }, function(data) {
      $("#state").text(data.result);
    });
    return false;
  });
});