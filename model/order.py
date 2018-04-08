class DoorState:
    NO_RESPONSE = 0
    NOT_OPEN = 1
    OPENED = 2
    CLOSED = 9


class OrderData:
    def __init__(self, order_id, total_fee, goods_name, goods_detail, date, paid=True):
        self.id = order_id
        self.title = "总金额"
        self.title_detail = "￥" + total_fee
        self.detail = [
            {"title": "商品名称", "title_detail": goods_name},
            {"title": "商品详情", "title_detail": goods_detail},
            {"title": "交易日期", "title_detail": date}
        ]
        if paid:
            self.button = "查看详情"
        else:
            self.button = "立即支付"
