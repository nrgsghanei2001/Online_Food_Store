$( document ).ready(function() {
    $("#submit").click("input", function() {
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'food' :$("#food :selected").val(),
            'price': $("#price").val(),
            'number': $("#number").val(),
            };
        console.log(data);
        alert("add")
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