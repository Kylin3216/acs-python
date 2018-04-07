function openDoor(door) {
    $.showLoading('开门中...');
    $.get("/openDoor/" + door, function (data) {
        if (data === "ok") {
            $.hideLoading();
            $.toast('开门成功！');
            $("a").addClass("weui-btn_disabled");
            $("#wait").removeAttr("hidden")
            checkDoor();
        }
    });
}

function checkDoor() {
    $.get("/checkDoorState", function (data) {
        if (data === "ok") {
            $("a").removeClass("weui-btn_disabled");
        } else {
            setTimeout(function () {
                checkDoor();
            }, 1000)
        }
    })
}