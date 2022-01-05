$( document ).ready(function() {
    $("button").click(function(e) {
        // if (e.target.className.search("delete-item") != -1){
        // insideText = e.target.parentElement.textContent;
        menu_item_id = e.target.id;
        // }
        number = $(`#number_${menu_item_id}`).val()
        // console.log(x)
        send_ajax()
    });

    function send_ajax(){
        
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'menu_item' : menu_item_id,
            'number' : number,
            };
        console.log(data);
        // console.log("data");

        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            
            success: function(res) {
                console.log(res);
                alert("added");
                // show_cats(res)
                // console.log("res");
                // show_persons(res)
            },
            always: function() {
                console.log(data);
            }
        });
    };
})
