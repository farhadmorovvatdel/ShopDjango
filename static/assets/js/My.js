$(document).ready(function (){
    $('#LoginForm').submit(function (event){

    var isValid=true;
    $('.error-message').empty();
    var mobile=$('#LoginMobile').val()
    var password=$('#LoginPassword').val()
        if(mobile ===''){
         $('#mobile-error').text("لطفا موبایل خود را وارد نمایید")
            isValid=false
        }
        if(mobile !='' && mobile.length<11) {
            $('#mobile-error').text("شماره موبایل باید 11 رفمی باشد")
            isValid = false
        }
         if(mobile !='' && mobile.length>11)
         {
              $('#mobile-error').text("شماره موبایل باید 11 رفمی باشد")
            isValid=false
         }

         if(!password){
         $('#password-error').text("لطفا رمز عبور خود را وارد نمایید")
            isValid=false
        }
           if (!isValid) {
            event.preventDefault();
        }
    })
})
 $(document).ready(function() {
            $('#LoginForm').submit(function(event) {
                event.preventDefault();
                $.ajax({
                    type: 'POST',
                    url: $(this).attr('action'),
                    data: $(this).serialize(),
                    dataType: 'json',
                    success: function (response) {
                        if (response.result === 'error') {
                            $('#login-error').text("کاربری با مشخصات فوق یافت نشد")
                        } else
                        {
                            window.location.href = "http://localhost:8001/users/profile"
                        }

                    }

                    });
            })
      });
$(document).ready(function (){
    $('#RegisterFormId').submit(function (event){

    var isValid=true;
    $('.error-message').empty();
    var Registermobile=$('#RegisterMobile').val()

    var password=$('#RegisterPassword').val()

    var repassword=$('#RegisterRePassword').val()
        if(Registermobile ===''){
         $('#Rmobile-error').text("لطفا موبایل خود را وارد نمایید")
            isValid=false
        }
        // if(Registermobile!=""  && Registermobile.length<11 ){
        //     $('#Rmobile-error').text("شماره موبایل باید 11 رقم باشد")
        //     isValid=false
        // }
         if(password ===''){
         $('#Rpassword-error').text("لطفا رمز عبور خود را وارد نمایید")
            isValid=false
        }
         if(password!=repassword){
             $('#match-error').text("رمزهای عبور با هم مغایرت دارند")
            isValid=false
         }
          if(password ===''){
                  $('#repassword-error').text("لطفا  تکرار رمز عبور خود را وارد نمایید")
            isValid=false
        }

           if (!isValid) {
            event.preventDefault();
        }
    })
})

 //
 // $(document).ready(function() {
 //            $('#RegisterFormId').submit(function(event) {
 //                event.preventDefault();
 //                $.ajax({
 //                    type: 'POST',
 //                    url: $(this).attr('action'),
 //                    data: $(this).serialize(),
 //                    dataType: 'json',
 //                    success: function (res) {
 //                        if (res.response === 'found') {
 //                            $('#phone-error').text("شماره موبایل تکراری می باشد")
 //                        }
 //                     if (res.response === 'success') {
 //                             window.location.href = "/users/profile";
 //                      }
 //
 //                    }
 //
 //                    });
 //            })
 //      });

