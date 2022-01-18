$( document ).ready(function() {
    $("#add").click("input", function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'restaurant' : $("#restaurant :selected").val(),
            'city': $("#city").val(),
            'address' :$("#address").val(),
            'category': $("#category :selected").val(),
            'meal': $("#meal :selected").val(),
            'details': $("#details").val(),
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