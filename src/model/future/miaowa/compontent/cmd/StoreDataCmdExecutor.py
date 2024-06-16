# coding=utf-8
import time
import pandas as pd
import os
from datetime import datetime

from src.model.future.miaowa.compontent.LogUtil import LogUtil
from src.model.future.miaowa.compontent.cmd.CmdExecutor import CmdExecutor


# 店铺数据爬取 执行
class StoreDataCmdExecutor(CmdExecutor):

    __base_path = "https://www.aliexpress.com/store/"
    _store_id_map = {
        "sport": "1101341831",
        "sport2": "1102689183"
    }

    def register(self, subparsers):
        parser = subparsers.add_parser('sd', help='子命令storeData(sd), 获取店铺数据')
        pass

    def execute(self, robot):
        sk = robot.context.getStoreCode()
        robot.browser.get(self.getStoreUrl(sk))
        count = 0
        while 1:
            start = time.clock()
            count = count + 1
            try:
                follower = robot.browser.get_driver().find_element_by_css_selector('#hd > div > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(2) > div > div:nth-child(3) > div:nth-child(1) > span:nth-child(1)').text.rstrip()
                score = robot.browser.get_driver().find_element_by_css_selector(
                    '#hd > div > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div > div > div:nth-child(2) > div > a > p').text.split(
                    " ")[0]
                end = time.clock()
                LogUtil.debug(f'第{count}次找到follower数据，耗时{end-start}ms')
                break
            except:
                time.sleep(1)
                LogUtil.debug("还未找到follower数据!")
                if count > 30:
                    msg = "未定位到店铺，可能被拦截"
                    LogUtil.error(msg)
                    raise Exception(msg)
        # 读取现有的Excel文件
        file_path = sk + '_data.xlsx'
        # 检查文件是否存在
        if os.path.exists(file_path):
            # 读取现有的Excel文件
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            # 创建一个空的DataFrame
            df = pd.DataFrame(columns=['日期', '评分', 'follower'])
        data = {
            "日期": [str(datetime.now())],
            "评分": [score],
            "follower": [follower]
        }
        new_row = pd.DataFrame(data)
        # 将原DataFrame和新DataFrame合并
        df_updated = pd.concat([df, new_row], ignore_index=True)

        # 将合并后的DataFrame保存回Excel文件
        df_updated.to_excel(file_path, index=False, engine='openpyxl')

        LogUtil.info(f"保存数据成功 {file_path}")
        pass

    def getStoreUrl(self, storeKind):
        return self.__base_path + self._store_id_map[storeKind]

