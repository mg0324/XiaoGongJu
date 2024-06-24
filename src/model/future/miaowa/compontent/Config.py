# coding=utf-8
# 配置类
import os


class Config:
    # 系统版本
    version = "1.2.1-20240619"
    # follow消息
    follow_msg = "Dear friend, \n Please follow my shop, I will thank you very much！\n [Admire]"
    # 评价内容
    review_msg = "You are a very good buyer, looking forward to your next purchase and hope you follow my shop"
    # 尝试刷新下一步的次数
    try_count = 10

    @staticmethod
    def get_config_path(config_dir, store_kind, config_type):
        return config_dir + "/" + store_kind + "/" + config_type + ".json"

    @staticmethod
    def getDefaultConfigDir():
        return os.path.expanduser("~") + f"/.xgj/miaoWa"

    @staticmethod
    def getMiaoWaVersion():
        return Config.version

