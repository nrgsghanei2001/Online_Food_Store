$( document ).ready(function() {

    $("#search").click(function(e) {
        
        // alert($("#in_text").val());
        send_ajax($("#in_text").val())
        e.preventDefault()
    });

    function send_ajax(input_data){
        data={
            'csrfmiddlewaretoken':CSRF_TOKEN,
            'name':input_data
            };
        $.ajax({
            type: 'POST',
            url: URL,
            dataType: 'json',
            data:data,
            success: function(res) {
                console.log(res);
                show_items(res)
            }
        });
    }
    
    function show_items(data){
        my_ul_tag = $('#mu_ul')
        my_ul_tag.empty()
        for (obj in data) {
            o = data[obj]
            var li = document.createElement("li");  
            var createA = document.createElement('a');
            var createAText = document.createTextNode('go to menu');
            createA.setAttribute('href', `all/restaurants/menu/${o['link']}`);
            createA.appendChild(createAText);
            /////////////////////////////////////////
            var createA2 = document.createElement('p');
            createA.append(o['name']);
            var createA3 = document.createElement('p');
            createA.append(o['price']);

            li.append(createA)
            li.append(createA2)
            li.append(createA3)
            my_ul_tag.append(li)
        }
        // if ( data['items'] ){
        //     // for (obj in data['items']) {
        //     //     var li = document.createElement("li");  
        //     //     var span1 = document.createElement("span");   
        //     //     span1.append(obj.price)
        //     //     li.append(span1)
        //     //     my_ul_tag.append(li)
        //     // }

        //     // for (const [key, value] of Object.entries(data['items'])) {
        //     //     console.log("*", key, value);
        //     //     var li = document.createElement("li");  
        //     //     var span1 = document.createElement("span");   
        //     //     span1.append(value)
        //     //     li.append(span1)
        //     //     my_ul_tag.append(li)
        //     //     }
            
        // }else{
        //     my_ul_tag.append()
        // }
        
    }
});