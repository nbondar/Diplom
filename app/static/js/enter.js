function enter()
  {
    var email = $("#email").val();
    //var nickname = $("#nickname").val();
    var password = $("#password").val();
    console.log(email);
    var remember_me = $("#remember_me").val();
    var json_to_send = {"email": email, "password": password, "remember_me": remember_me};
    $.ajax({
                url: '/enter',
                type: 'post',
                data: JSON.stringify(json_to_send),
                contentType: 'application/json',
                dataType: 'json',
                timeout: 0
            }).done(function (result){
                if (result.result["status"]=="OK")
                {
                    window.location.href="/dashboard";
                }
                else
                {
                    var el = $("#Error");
                    var str = "Ошибка:  Такой комбинации логина/пароля нет в системе!!!";
                    el.innerText = str;
                    el.html(str).fadeIn();
                }
                //if (result.result["status"]=="OK")
            });
    };