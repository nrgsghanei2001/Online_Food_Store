$( document ).ready(function() {
    $("#submit").click("input", function() {
        console.log("xxxxxxxxxxx")
        send_ajax()
    });

    function send_ajax(){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            // 'name' : $("#name").value,
            // 'detail': $("#detail").innerHTML(),
            // 'category': $("#category").innerHTML(),
            // 'meal': $("#meal").innerHTML(),
            // 'image': $("#image").val(),
            'name' : $("#name").val(),
            'detail': $("#detail").val(),
            'category' :$("#category :selected").text(),
            'meal': $("#meal :selected").text(),
            'image': $("#image").val(),
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
                // console.log("res");
                // show_persons(res)
            },
            always: function() {
                console.log(data);
            }
        });
    }
});