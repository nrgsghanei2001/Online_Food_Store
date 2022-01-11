$( document ).ready(function() {
    $("button").click(function(e) {
        item_id = e.target.id;
        if (e.target.name == "delete") {
            action = "delete"
            send_ajax()
        }
        else {
            action = "edit"
            send_ajax()
        }
    });

    function send_ajax(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'item_id' : item_id,
            'action':action,
            };
        console.log(data);

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
    };
})
