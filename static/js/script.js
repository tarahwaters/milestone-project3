/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
    $('textarea#cafe_description').characterCounter();
  });