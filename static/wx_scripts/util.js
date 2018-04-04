function isWx() {
    let ua = window.navigator.userAgent.toLowerCase();
    return !!ua.match(/MicroMessenger/i);
}

/**
 * 判断是否在支付宝端
 * @returns {boolean}
 */
function isAp() {
    let ua = window.navigator.userAgent.toLowerCase();
    return !!ua.match(/AlipayClient/i);
}