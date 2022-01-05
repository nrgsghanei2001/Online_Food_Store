$( document ).ready(function() {
    $("button").click(function(e) {
        send_ajax()
    });

    function send_ajax(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            };
        console.log(data);

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
                alert("added");
            },
            always: function() {
                console.log(data);
            }
        });
    };
})
