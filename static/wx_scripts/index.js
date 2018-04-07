function scanCode() {
    location.href = "/doQrCode?qrCode=1234";

   /* wx.scanQRCode({
        needResult: 1, // 默认为0，扫描结果由微信处理，1则直接返回扫描结果，
        scanType: ["qrCode"], // 可以指定扫二维码还是一维码，默认二者都有
        success: function (res) {
            let result = res.resultStr; // 当needResult 为 1 时，扫码返回的结果
            if (configQrCode(result)) {
                location.href = "/doQrCode?qrCode=" + result
            } else {
                $.alert("不是有效的二维码");
            }
        }
    });*/
}

function configQrCode(code) {
    if (!!code.match(/www.elviracheng.com/i)) {
        if (!!code.match(/door/i)) {
            return true;
        }
    }
    return false;
}