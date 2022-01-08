$( document ).ready(function() {
    $("button").click(function(e) {
        food_id = e.target.id;
        if (e.target.name == "remove") {
            send_ajax()
        }
        else {
            send_ajax2()
        }
    });

    function send_ajax(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'food' : food_id,
            };
        console.log(data);

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
                alert("deleted");
            },
            always: function() {
                console.log(data);
            }
        });
    };

    function send_ajax2(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'food' : food_id,
            };
        console.log(data);

        $.ajax({
            type: 'POST',
            url: URL2,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
                alert("OK")
            },
            always: function() {
                console.log(data);
            }
        });
    };
})
