$( document ).ready(function() {
    $("button").click(function(e) {
        address_id = e.target.id
        if (address_id == "edit") {
            send_ajax()
        }
        else {
            send_ajax1()
        }
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
    function send_ajax1(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'address_id': address_id,
            };
        console.log(data);
        console.log("data");

        $.ajax({
            type: 'POST',
            url: URL2,
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