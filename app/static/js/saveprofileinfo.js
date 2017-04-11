function saveprofileinfo(email)
{
	//var el = $("#email");
	//var email = el.val();
	var nickname = $("#nickname").val();
    var name = $("#name").val();
    var surname = $("#surname").val();
    var phonenumber = $("#phonenumber").val();

    var json_to_send = {"email": email, "nickname": nickname, "surname": surname, "name": name, "phonenumber": phonenumber};
    $.ajax({
                url: '/saveprofile',
                type: 'post',
                data: JSON.stringify(json_to_send),
                contentType: 'application/json',
                dataType: 'json',
                timeout: 0
            }).done(function (result){
                if (result.result["status"]=="OK")
                {
                	window.location.href="/profile";
                    //console.log(result.result["status"])
                    //window.location.href="/ok";
                }
                else
                {
                	alert("Error")
                }
});
};