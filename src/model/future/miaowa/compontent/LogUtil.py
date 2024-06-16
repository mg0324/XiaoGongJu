# coding=utf-8
# 日志工具
import logging.config
import logging

from src.model.future.miaowa.compontent.Config import Config

# 先加载配置
logging.config.fileConfig(Config.getDefaultConfigDir() + '/logging.conf')
# 使用配置文件中的Logger
logger = logging.getLogger('my_logger')


class LogUtil:
    @staticmethod
    def info(msg):
        logger.info(msg)
        pass

    @staticmethod
    def debug(msg):
        logger.debug(msg)
        pass

    @staticmethod
    def warning(msg):
        logger.warning(msg)
        pass

    @staticmethod
    def error(msg):
        logger.error(msg)
        pass

    @staticmethod
    def getLogger():
        return logger


