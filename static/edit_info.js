$( document ).ready(function() {
    $("#edit").click(function() {
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'email' : $("#email").val(),
            'city': $("#city").val(),
            'address': $("#address").val(),
            };
        console.log(data);
        console.log("data");

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
            },
            always: function() {
                console.log(data);
            }
        });
    }
});