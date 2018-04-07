function submit() {
    if (checkTel() && checkCode() && checkCheck()) {
        $.showLoading("请稍后...")
        $.post('/login', $("form").serialize(), function (data) {
            if (data === "ok") {
                setTimeout(function () {
                    $.hideLoading()
                    $.toast("提交成功");
                }, 1500);
            } else {
                $.hideLoading();
                $.toast(data, "forbidden");
            }
        })
    }
    $.hideLoading();
}

$("form input:even").blur(function () {
    checkTel();
})
$("form input:odd").blur(function () {
    checkCode();
})
$("form button").click(function () {
    if (checkTel()) {
        $(this)[0].disabled = true;
        let that = $(this);
        let interval = 10;
        $.get('/getSmsCode/' + $("form input:first").val(), function (data) {
            if (data === "ok") {
                that.text(interval + "s后重试");
                let val = setInterval(() => {
                    interval--;
                    that.text(interval + "s后重试");
                    if (interval < 0) {
                        that.text("获取验证码");
                        that[0].disabled = false;
                        clearInterval(val);
                    }
                }, 1000)
            } else {
                $.toast("网络错误，请稍后重试", "forbidden");
                that[0].disabled = false;
            }
        })
    }
})

function checkTel() {
    let tel = $("form input")[0];
    if (!tel.value) {
        $.toptip("请输入手机号", 'error')
        return false;
    }
    if (!validateTel(tel.value)) {
        $.toptip("手机号格式不正确", 'error')
        return false;
    }
    return true;
}

function checkCode() {
    let code = $("form input")[1];
    if (!code.value) {
        $.toptip("请输入验证码", 'error')
        return false;
    }
    return true;
}

function checkCheck() {
    let check = $("input:last")[0];
    if (!check.checked) {
        $.toptip("请阅读并同意协议", 'error')
        return false;
    }
    return true;
}


function validateTel(value) {
    let regex = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    return regex.test(value);
}