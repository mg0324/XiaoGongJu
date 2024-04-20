# coding=utf-8
from src.model.future.miaowa.compontent.order.LoadJsonOrderStrategy import LoadJsonOrderStrategy
from src.model.future.miaowa.compontent.order.SpiderOrderStrategy import SpiderOrderStrategy


# 订单管理器
class OrderManager:

    # 类型实现
    __impl = {
        "json": LoadJsonOrderStrategy(),
        "spider": SpiderOrderStrategy()
    }

    @staticmethod
    def get_instance(impl):
        return OrderManager.__impl.get(impl)
