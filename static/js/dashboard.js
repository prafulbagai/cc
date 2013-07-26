$(function(){

    $(.reply).submit(function (event) {
        event.preventDefault();
        alert();
        /*//
        $.ajax({
            type: "POST",
            url: "/dashboard",
            data : {
                'reply_id' : $(this).attr('id');
                'reply' : $(this).children('input').val();
            },
            success: function(response) {
              //$(this).html()
            },
            error :function(response){

            }
        });
        //*/
        return false;
    });
});


