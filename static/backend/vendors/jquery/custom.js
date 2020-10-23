$(document).ready(function(){

$("#add").click(function(e){

$('#items').append('<div><div id="items"><input type="text"/></div>'
+'<input type="button" id="delete" class="btn btn-danger" value="Delete"/></div>');

});

$('body').on('click','#delete',function(e){
    $(this).parent('div').remove();
});

});