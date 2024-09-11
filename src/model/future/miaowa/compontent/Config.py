# coding=utf-8
# 配置类
import os
import json


class Config:
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
        return Config.getMiaoWaConfig()["version"]

    @staticmethod
    def getMiaoWaConfig():
        with open(Config.getDefaultConfigDir() + "/config.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def getCanReviewDays():
        return Config.getMiaoWaConfig()["review"]["days"]

    @staticmethod
    def getCanReviewScore():
        return Config.getMiaoWaConfig()["review"]["score"]

    @staticmethod
    def getMiaoWaStoreList():
        return Config.getMiaoWaConfig()["stores"]

    @staticmethod
    def getFollowMsg():
        return Config.getMiaoWaConfig()["followMsg"]

    @staticmethod
    def getReviewMsg():
        return Config.getMiaoWaConfig()["reviewMsg"]

    @staticmethod
    def getTryCount():
        return Config.getMiaoWaConfig()["tryCount"]
