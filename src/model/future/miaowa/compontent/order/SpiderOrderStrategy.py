# coding=utf-8
import time
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.compontent.order.OrderStrategy import OrderStrategy


# 从star view中获取星值 0-0星，20-一星，40-二星，60-三星，80-4星，100-5星
def get_star_from_star_view(element):
    style = element.find_element_by_css_selector("span").get_attribute("style")
    return int(style.replace("width:", "").replace("%;",""))


# 爬虫
class SpiderOrderStrategy(OrderStrategy):
    order_list = []

    # 基于爬虫，获取页面待处理的订单号列表
    def fetch_order_list(self, robot):
        # 打开评价首页
        robot.browser.get(robot.store.review_url+"?page="+robot.context.getPage())
        prefix = "[store="+robot.store.get_name()+"]"
        while 1:
            start = time.time()
            try:
                order_table = robot.browser.get_driver().find_element_by_id("buyer-ordertable")
                LogUtil.debug(prefix + '已定位到买家订单表格[buyer-ordertable]')
                end = time.time()
                break
            except:
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到买家订单表格[buyer-ordertable]!")

        LogUtil.debug(prefix + '定位耗费时间：' + str(end - start))
        # 找到tbody
        tbody_list = order_table.find_elements_by_tag_name("tbody")
        for tbody in tbody_list:
            # 订单号
            order_number = tbody.find_element_by_class_name("order-head").find_element_by_class_name("info-body").text
            feedback = tbody.find_element_by_class_name("product-feedback")
            views = feedback.find_elements_by_class_name("star-view")
            my_star = get_star_from_star_view(views[0])
            buyer_star = get_star_from_star_view(views[1])
            # 4星以上是好评，且自己没有评过分
            if buyer_star >= 80 and my_star == 0:
                self.order_list.append(order_number)
                LogUtil.debug(prefix + "order_number="+order_number+",my_star="+str(my_star)+",buyer_star="+str(buyer_star))
        return self.order_list

