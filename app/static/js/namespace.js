function namespace(id_n)
{
	console.log("fuck");
	var id = id_n;
	var namespace = $("#namespace").val();
	console.log(namespace);
	var timestamp = Date();
	console.log(timestamp);
	var json_to_send = {"id_u": id, "name": namespace, "timestamp": timestamp};
    $.ajax({
                url: '/namespace',
                type: 'post',
                data: JSON.stringify(json_to_send),
                contentType: 'application/json',
                dataType: 'json',
                timeout: 0
            }).done(function (result){
            	if (result.result["status"]=="OK")
                {
                	
                    window.location.href="/newnamespace";
                }
                else
                {
                	alert(result.result["status"]);
                }
            });
	
};