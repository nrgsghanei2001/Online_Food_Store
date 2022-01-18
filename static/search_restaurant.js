$( document ).ready(function() {

    $("#search").click(function(e) {
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
        my_ul_tag = $('#searched')
        my_ul_tag.empty()
        for (obj in data) {
            o = data[obj]
            var div1 = document.createElement("div");
            div1.className = "col-sm-4";
            var div2 = document.createElement("div");
            div2.className = "panel panel-primary";
            var div3 = document.createElement("div");
            div3.className = "panel-heading";
            var div4 = document.createElement("div");
            div4.className = "panel-body";
            var div5 = document.createElement("div");
            div5.className = "panel-footer";
            ////////////
            var createA = document.createElement('a');
            createA.className = "btn btn-warning";
            var createAText = document.createTextNode('show');
            createA.style.color = "black";
            createA.setAttribute('href', `/all/restaurants/${o['link']}`);
            createA.appendChild(createAText);
            //////////
            var createA2 = document.createElement('h3');
            var createAText1 = document.createTextNode(`${o['name']}`);
            createA2.appendChild(createAText1);
            /////////
            var createA3 = document.createElement('p');
            var createAText2 = document.createTextNode(`category: ${o['category']}, meal: ${o['meal']}`);
            createA3.appendChild(createAText2);
            createA3.style.color = "black";
            div3.append(createA2);
            div4.append(createA3);
            div5.append(createA);
            div1.append(div2);
            div2.append(div3);
            div2.append(div4);
            div2.append(div5);
            my_ul_tag.append(div1);
        }     
    }
});