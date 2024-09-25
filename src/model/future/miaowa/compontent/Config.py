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
    def get_default_config_dir():
        return os.path.expanduser("~") + f"/.xgj/miaoWa"

    @staticmethod
    def get_miao_wa_version():
        return Config.get_miao_wa_config()["version"]

    @staticmethod
    def get_miao_wa_config():
        with open(Config.get_default_config_dir() + "/config.json", 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def get_can_review_days():
        return Config.get_miao_wa_config()["review"]["days"]

    @staticmethod
    def get_can_review_score():
        return Config.get_miao_wa_config()["review"]["score"]

    @staticmethod
    def get_miao_wa_store_list():
        return Config.get_miao_wa_config()["stores"]

    @staticmethod
    def get_follow_msg():
        return Config.get_miao_wa_config()["followMsg"]

    @staticmethod
    def get_review_msg():
        return Config.get_miao_wa_config()["reviewMsg"]

    @staticmethod
    def get_try_count():
        return Config.get_miao_wa_config()["tryCount"]

    @staticmethod
    def get_chrome_driver_path():
        return Config.get_miao_wa_config()["chromeDriverPath"]
