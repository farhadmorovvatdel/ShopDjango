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
            $('#mobile-error').text("شماره موبایل باید 11 رقمی باشد")
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
               setTimeout(function () {
                   $('.error-message').empty()

               }, 3000);
           }
            event.preventDefault();
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
                        setTimeout(function () {
                              $('#login-error').empty()

                     }, 3000);

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
               setTimeout(function () {
                   $('.error-message').empty()

               }, 3000);
           }
            event.preventDefault();
    })
})


 // $(document).ready(function() {
 //            $('#RegisterFormId').submit(function(event) {
 //                event.preventDefault();
 //                $.ajax({
 //                    type: 'POST',
 //                    url: $(this).attr('action'),
 //                    data: $(this).serialize(),
 //                    dataType: 'json',
 //                    success: function (res) {
 //                        if (res.response ==='found') {
 //                            $('#notphone-error').text("شماره موبایل تکراری می باشد")
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

 $(document).ready(function() {
        $('.color-box').on('click', function() {
            // حذف کلاس 'selected' از تمام رنگ‌ها
            $('.color-box').removeClass('selected');
            // اضافه کردن کلاس 'selected' به رنگ انتخاب شده
            $(this).addClass('selected');
            // به‌روزرسانی فیلد مخفی با رنگ انتخاب شده
            $('#selected-color').val($(this).data('color'));
            // چاپ رنگ انتخاب شده در کنسول برای تست
            console.log('Selected color:', $(this).data('color'));
        });
    });

 $(document).ready(function() {
        $('.size-box').on('click', function() {
            // حذف کلاس 'selected' از تمام سایزها
            $('.size-box').removeClass('selected');
            // اضافه کردن کلاس 'selected' به سایز انتخاب شده
            $(this).addClass('selected');
            // به‌روزرسانی فیلد مخفی با سایز انتخاب شده
            $('#selected-size').val($(this).data('size'));
            // چاپ سایز انتخاب شده در کنسول برای تست
            console.log('Selected size:', $(this).data('size'));
        });
    });
// Add Faviorate Product
   $(document).ready(function() {
        $('.add-to-favorites').on('click', function(event) {
            event.preventDefault();

            var url = $(this).attr('href');
            console.log(url)
            var productId = $(this).data('product-id');
            console.log(productId)

            $.ajax({
                type: 'GET',
                url: url,
                data: {
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                success: function(response) {
                    var message= $('#fave-message')
                    if (response.status === 'Found') {
                   message.text("این محصول قبلا به لیست علاقه مندی اضافه شده است")
                   message.css('background', 'red')
                   message.show()

                    }

                    else if (response.status === 'Added') {
                        message.text("محصول پسندیده شد")
                       message.css('background', 'green')
                       message.show()
                    }
                    setTimeout(function() {
                        message.fadeOut();
                    }, 3000);
                },

            });
        });
    });
// ChangePasswordForm
$(document).ready(function (){
    $('#Passchange_form').submit(function (event){
        var isValid=true;
        $('.password_error').empty();
        var cussrentpassword=$('#CurrentPassword_id').val()
        var newpass=$('#ChangePassword_id').val()
        var newpass2=$('#ChanegRePassword_id').val()
        if(cussrentpassword === '') {
          $('#currentpassword').text('لطفا رمز عبور فعلی را وارد نمایید')
          $('#currentpassword').show()
            isValid=false

        }
        else if(newpass === ''){
        $('#newpassword').text('لطفا رمز عبور جدید را وارد نمایید')
            $('#newpassword').show()
            isValid=false
        }

        else if(newpass2===''){
            $('#newrepassword').text('لطفا  تکرار رمز عبور جدید را وارد نمایید')
             $('#newrepassword').show()
            isValid=false
           }
        else if(newpass!=newpass2){
        $('#matchpassword').text('رمزهای عبور جدید با هم مغایرت دارند')
         $('#matchpassword').show()
            isValid=false
           }

        if (!isValid) {
            setTimeout(function() {
                $('.password_error').empty()
                  $('.password_error').hide();

            }, 3000);

            event.preventDefault();
        }

    })
})

  $(document).ready(function() {
        $('#Passchange_form').on('submit', function(event) {
            event.preventDefault();
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'),
                data: $(this).serialize(),
                success: function(response) {
                    if (response.status === 'success') {
                        $('.success_message').text('رمز عبور شما با موفقیت تغییر یافت')
                        $('.success_message').show()
                       setTimeout(function() {
                        $('.success_message').empty();
                         $('.success_message').hide()
                        window.location.href = "/users/logout";
                    }, 2000);
                    } else if(response.status ==='error') {

                       $('#error_pas').text('رمز عبور فعلی صحیح نمی باشد')
                       $('#error_pas').show()
                        setTimeout(function() {

                        $('#error_pas').empty();
                        $('.password_error').hide();
                    }, 3000);
                    }
                },
                error: function(xhr, status, error) {
                    alert('خطا: ' + error);
                }
            });
        });
    });
//Remove Faviorate Product/////
$(document).ready(function() {
function getCsrfToken() {
            return $('meta[name="csrf-token"]').attr('content');
        }
    $('.e-remove-product').on('click', function (event) {
        event.preventDefault()
        var url = $(this).data('url');
        var item_id=$(this).data('item')
        $.ajax({
            type:'POST',
            url:url,
             headers: {
                'X-CSRFToken': getCsrfToken()
             },
             success:function (res){
                if(res.status ==='NotFound'){
                    $('#nofavpr').empty();
                    $('#nofavpr').text("محصولی در لیست علاقه مندی ها موجود نمی باشد");
                    $('#nofavpr').css({
                    'background-color': '#fff',
                    'border': '1px solid #ddd',
                    'border-radius': '5px',
                    'padding': '20px',
                    'text-align': 'center',
                    'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)',
                    'color': 'red'

                    })

                }
             },
        })

    })
});

