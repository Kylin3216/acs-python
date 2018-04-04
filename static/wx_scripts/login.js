function submit() {
    if (checkTel() && checkCode() && checkCheck()) {
        let loading = weui.loading('请稍后...');
        $.post('/login', {name: $("#telephone").val(), code: $("#code").val()}, function (data) {
            if (data == "ok") {
                setTimeout(function () {
                    loading.hide();
                    weui.toast('提交成功', 3000);
                }, 1500);
            } else {
                loading.hide();
                weui.toast(data, 2000);
            }

        })
        loading.hide();
    }
}

$("#telephone").keydown(function () {
    hideError($(this)[0]);
})
$("#telephone").focus(function () {
    hideError($(this)[0]);
})
$("#code").keydown(function () {
    hideError($(this)[0]);
})
$("#code").focus(function () {
    hideError($(this)[0]);
})
$("#telephone").blur(function () {
    checkTel();
})
$("#code").blur(function () {
    checkCode();
})
$(".weui-vcode-btn").click(function () {
    if (checkTel()) {
        $(".weui-vcode-btn")[0].disabled = true;
        let interval = 10;
        $.get('/getSmsCode?telephone=' + $("#telephone").val(), function (data) {
            if (data == "ok") {
                $(".weui-vcode-btn").text(interval + "s后重试");
                let val = setInterval(() => {
                    interval--;
                    $(".weui-vcode-btn").text(interval + "s后重试");
                    if (interval < 0) {
                        $(".weui-vcode-btn").text("获取验证码");
                        $(".weui-vcode-btn")[0].disabled = false;
                        clearInterval(val);
                    }
                }, 1000)
            } else {
                weui.toast('网络错误，请稍后重试', 2000);
                $(".weui-vcode-btn")[0].disabled = false;
            }
        })
    }
})

function checkTel() {
    let tel = $("#telephone")[0];
    if (!tel.value) {
        showError(tel, "empty");
        return false;
    }
    if (!validateTel(tel.value)) {
        showError(tel, "notMatch");
        return false;
    }
    return true;
}

function checkCode() {
    let code = $("#code")[0];
    if (!code.value) {
        showError(code, "empty");
        return false;
    }
    return true;
}

function checkCheck() {
    let check = $("#check")[0];
    if (!check.checked) {
        showError(check, "empty");
        return false;
    }
    return true;
}

/*type=  empty  ||  notMatch*/
function showError(ele, type) {
    weui.form.showErrorTips({
        ele: ele,
        msg: type
    });
}

function hideError(ele) {
    weui.form.hideErrorTips(ele);
}

function validateTel(value) {
    let regex = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    if (regex.test(value)) {
        return true;
    }
    return false;
}