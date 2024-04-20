# coding=utf-8
# 店
from src.model.future.miaowa.compontent.Config import Config


class Store:
    # 订单详情页URL
    order_detail_url = "https://gsp.aliexpress.com/apps/order/detail?step=4&orderId="
    # 速卖通后台首页
    home_url = "https://gsp.aliexpress.com/apps/order/index"
    # 评价页
    review_url = "https://feedback.aliexpress.com/management/feedbackSellerList.htm"
    # 店的类型，sport-运动店; toy-玩具店 ; 默认sport
    __kind = "sport"
    # 是否登录
    __is_login = False

    def __init__(self, kind):
        self.__kind = kind
        pass

    # 是否登录
    def is_login(self):
        return self.__is_login

    # 获取cookies配置
    def get_cookies_path(self, context):
        return Config.get_config_path(context.getConfigDir(), self.__kind, "cookies")

    # 获取orders配置
    def get_orders_path(self):
        return Config.get_config_path(self.__kind, "orders")

    # 获取店名
    def get_name(self):
        return self.__kind

    # 设置登录状态
    def set_login(self, v):
        self.__is_login = v
        pass



