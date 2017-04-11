
function registration()
  {
    var email = $("#email").val();
    var nickname = $("#nickname").val();
    var password1 = $("#password1").val();
    var password2 = $("#password2").val();
    if (email == "" && nickname=="" && password1=="" && password2=="")
    {
      var el = $("#Error");
      var str = "Ошибка:  Все поля должны быть заполнены!!!";
      el.innerText = str;
      el.html(str).fadeIn();
    }
    else{
    if (password1 != password2)
    {
      var el = $("#Error");
      var str = "Ошибка:  Введенные пароли не совпадают!!!";
      el.innerText = str;
      el.html(str).fadeIn();
      
    }
    else{

    var json_to_send = {"email": email, "nickname": nickname, "password": password1};
    $.ajax({
                url: '/add',
                type: 'post',
                data: JSON.stringify(json_to_send),
                contentType: 'application/json',
                dataType: 'json',
                timeout: 0
            }).done(function (result){
                if (result.result["status"]=="OK")
                {
                    //console.log(result.result["status"])
                    window.location.href="/ok";
                }
                else
                {
                    //console.log(result.result["status"])
                    var el = $("#Error");
                    var str = "Ошибка:  Такой логин/пароль уже есть в системе!!!";
                    el.innerText = str;
                    el.html(str).fadeIn();
                }
                //if (result.result["status"]=="OK")
            });
    }
}
    };