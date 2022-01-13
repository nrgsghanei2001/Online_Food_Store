$( document ).ready(function() {
    $("#submit").click(function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'number' : $("#number").val(),
            'price': $("#price").val(),
            'name' :$("#name :selected").val(),
            };
        console.log(data);
        alert("edited")
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