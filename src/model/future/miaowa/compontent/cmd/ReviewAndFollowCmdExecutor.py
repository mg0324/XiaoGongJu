# coding=utf-8
import time

from src.model.future.miaowa.compontent.Config import Config
from src.model.future.miaowa.compontent.GetTime import GetTime
from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.compontent.cmd.CmdExecutor import CmdExecutor
from src.model.future.miaowa.compontent.order.OrderManager import OrderManager


# review and follow 执行
class ReviewAndFollowCmdExecutor(CmdExecutor):
    # 到详情页
    @GetTime("到详情页")
    def goto_detail(self, robot, order_number):
        robot.browser.switch_window(0)
        path = robot.store.order_detail_url + order_number
        robot.browser.get(path)
        pass

    def fetch_orders(self, robot):
        # 使用 load json方式
        # print(robot.argument.get_args())
        order_strategy = OrderManager.get_instance("spider")
        # print(order_strategy)
        orders = order_strategy.fetch_order_list(robot)
        LogUtil.info(f"[store={robot.store.get_name()}]本次处理订单列表为{str(orders)}")
        return orders

    def execute(self, robot):
        # 1.浏览器登录到店后台首页
        robot.login_to_home()
        # 2.获取订单列表
        orders = self.fetch_orders(robot)
        # 3.开始处理订单任务
        for order_number in orders:
            prefix = "[store=" + robot.store.get_name() + "]订单号=" + order_number
            # 打开详情页
            self.goto_detail(robot, order_number)
            LogUtil.info(prefix + "到详情页")
            self.do_follow(robot, order_number)
            self.do_review(robot, order_number)
        pass

    # 处理follow
    @GetTime("处理follow")
    def do_follow(self, robot, order_number):
        prefix = "[store=" + robot.store.get_name() + "][" + order_number + "]"
        LogUtil.debug(prefix + "开始处理follow")
        count = 1
        afterFlag = False
        while 1:
            start = time.time()
            try:
                robot.browser.get_driver().find_element_by_link_text('Contact').click()
                LogUtil.debug(prefix + '已点击联系买家链接')
                end = time.time()
                break
            except:
                count = count + 1
                if count > Config.try_count:
                    afterFlag = True
                    break
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到元素!")
        if afterFlag:
            LogUtil.error(prefix + "已过联系时间，不再处理")
            return 1
        LogUtil.debug(prefix + "定位耗费时间：" + str(end - start))
        robot.browser.switch_window(1)
        robot.browser.get_driver().execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
        })
        # 评论框class
        textareaClass = "im-message-input-input-wrap"
        count = 1
        afterFlag = False
        while 1:
            start = time.time()
            try:
                robot.browser.get_driver().find_element_by_class_name(textareaClass)
                LogUtil.debug(prefix + textareaClass + '已定位到元素')
                end = time.time()
                break
            except:
                count = count + 1
                time.sleep(1)
                if count > Config.try_count:
                    afterFlag = True
                    break
                LogUtil.debug(prefix + textareaClass + "还未定位到元素!")
        if afterFlag:
            LogUtil.error(prefix + "无法定位到消息框，退出!")
            robot.browser.close()
            return 1
        LogUtil.debug(prefix + textareaClass + '定位耗费时间：' + str(end - start))
        # 找到评价框
        textarea = robot.browser.get_driver().find_element_by_css_selector("."+textareaClass+" textarea")
        textarea.send_keys(robot.config.follow_msg)
        time.sleep(1)
        js = "var q=document.querySelector('#root > div:nth-child(3) > div > div.csp-im_im-message-content > div > div > div.csp-im_message-container > div > div.im-message-box-addon-after > div > div > footer > div.im-message-input-footer-right > a > i > svg').parentElement.click()"
        # robot.browser.get_driver().execute_script(js)
        # document.getElementsByClassName('im-icon-paper-plane').children[0].click()
        # browser.find_element_by_class_name("im-icon-paper-plane").click()
        time.sleep(2)
        robot.browser.close()
        pass

    # 处理review
    @GetTime("处理review")
    def do_review(self, robot, order_number):
        prefix = "[store=" + robot.store.get_name() + "][" + order_number + "]"
        LogUtil.debug(prefix + "开始处理review")
        # 切回到订单详情页，点击评价，进入评价页
        robot.browser.switch_window(0)
        count = 1
        afterFlag = False
        while 1:
            start = time.clock()
            count = count + 1
            try:
                robot.browser.get_driver().find_element_by_link_text('Review buyer').click()
                LogUtil.debug(prefix + '已点击评价按钮')
                end = time.clock()
                break
            except:
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到元素!")
                if count > Config.try_count:
                    afterFlag = True
                    break
        if afterFlag:
            LogUtil.debug(prefix + '已过评价时间')
            return 1

        LogUtil.debug(prefix + '定位耗费时间：' + str(end - start))

        robot.browser.switch_window(1)
        while 1:
            start = time.clock()
            try:
                robot.browser.get_driver().find_element_by_xpath('//*[@id="the-ratings"]/div/div[3]/span[5]').click()
                LogUtil.debug(prefix + '已点击5星')
                end = time.clock()
                break
            except:
                time.sleep(1)
                LogUtil.debug(prefix + "还未定位到元素!")

        LogUtil.debug(prefix + '定位耗费时间：' + str(end - start))
        # 评价内容
        robot.browser.get_driver().find_element_by_id('the-form-message').send_keys(robot.config.review_msg)
        # 点击评价
        robot.browser.get_driver().find_element_by_id('feedback-submit-button').click()
        # 关闭
        robot.browser.close()
        pass

