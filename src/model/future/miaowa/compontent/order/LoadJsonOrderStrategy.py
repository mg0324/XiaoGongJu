# coding=utf-8
import json

from src.model.future.miaowa.compontent.order.OrderStrategy import OrderStrategy


# 从json文件里加载
class LoadJsonOrderStrategy(OrderStrategy):

    # 从json文件里获取
    def fetch_order_list(self, robot):
        path = robot.store.get_orders_path()
        with open(path) as f:
            self.order_list = json.loads(f.read())
        return self.order_list
