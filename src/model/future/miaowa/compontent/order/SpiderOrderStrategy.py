# coding=utf-8
import time
from datetime import datetime, timedelta

from src.model.future.miaowa.compontent.Config import Config
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.compontent.order.OrderStrategy import OrderStrategy


# 从star view中获取星值 0-0星，20-一星，40-二星，60-三星，80-4星，100-5星
def get_star_from_star_view(element):
    style = element.find_element_by_css_selector("span").get_attribute("style")
    return int(style.replace("width:", "").replace("%;", ""))


# 判断是否在指定天数内
def is_in_days(close_date, days):
    # 获取当前时间
    current_time = datetime.now()

    # 计算当前时间和输入时间的差异
    time_difference = current_time - close_date

    # 判断是否在一个月内（假设一个月为30天）
    if abs(time_difference) <= timedelta(days=days):
        return True
    else:
        return False


# 爬虫
class SpiderOrderStrategy(OrderStrategy):
    order_list = []

    # 基于爬虫，获取页面待处理的订单号列表
    def fetch_order_list(self, robot):
        # 打开评价首页
        robot.browser.get(robot.store.review_url+"?page="+robot.context.getPage())
        prefix = "[store="+robot.store.get_name()+"]"
        count = 1
        afterFlag = False
        while 1:
            start = time.perf_counter()
            try:
                order_table = robot.browser.get_driver().find_element_by_id("buyer-ordertable")
                LogUtil.debug(prefix + '已定位到买家订单表格[buyer-ordertable]')
                end = time.perf_counter()
                break
            except:
                time.sleep(1)
                count = count + 1
                LogUtil.debug(prefix + "还未定位到买家订单表格[buyer-ordertable]!")
                if count > Config.try_count:
                    afterFlag = True
                    break
        if afterFlag:
            LogUtil.debug(prefix + '请检查登陆信息是否失效！')
            return None

        LogUtil.debug(prefix + '定位耗费时间：' + str(end - start))
        # 找到tbody
        tbody_list = order_table.find_elements_by_tag_name("tbody")
        for tbody in tbody_list:
            # 订单号
            order_number = tbody.find_element_by_class_name("order-head").find_element_by_class_name("info-body").text
            feedback = tbody.find_element_by_class_name("product-feedback")
            views = feedback.find_elements_by_class_name("star-view")
            # 订单关闭时间
            close_date_str = tbody.find_element_by_class_name("order-complayDate").find_element_by_class_name("info-body").text
            my_star = get_star_from_star_view(views[0])
            buyer_star = get_star_from_star_view(views[1])
            LogUtil.debug(prefix + "order_number=" + order_number + ",my_star=" + str(my_star) + ",buyer_star=" + str(buyer_star)
                + ",close_date_str=" + close_date_str)
            close_date = datetime.strptime(close_date_str, "%Y.%m.%d %H:%M")
            # 4星以上是好评，且自己没有评过分
            if buyer_star >= 80 and my_star == 0 and is_in_days(close_date, Config.getMiaoWaConfig()["review_days"]):
                self.order_list.append(order_number)
                LogUtil.info(prefix + "添加可raf订单：" + order_number)
        return self.order_list

