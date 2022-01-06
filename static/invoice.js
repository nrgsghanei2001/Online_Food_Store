$( document ).ready(function() {
    // $("button").click(function(e) {
    //     send_ajax()
    // });
    $("button").click(function(e) {
        // e.preventDefault()
        // console.log("hi")
        // alert("hi")
        order_item_id = e.target.id;
        if (order_item_id == "confirm") {
            send_ajax()
        }
        else {
            console.log(order_item_id)
            send_ajax1()
        }
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
    function send_ajax1(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'order_item':order_item_id,
            };
        console.log(data);

        $.ajax({
            type: 'POST',
            url: URL2,
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
})
