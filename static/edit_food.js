$( document ).ready(function() {
    $("#submit").click(function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'name' : $("#name").val(),
            'detail': $("#detail").val(),
            'category' :$("#category :selected").text(),
            'meal': $("#meal :selected").text(),
            'image': $("#image").val(),
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