#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: log_utils.py
# @time: 2020/7/5 2:24 下午

import os
import logging
import time
from common.localconfig_utils import local_config

current_path = os.path.dirname(__file__)
log_output_path = os.path.join( current_path,'..', local_config.LOG_PATH  )

class LogUtils():
    def __init__(self,log_path=log_output_path):
        self.log_name = os.path.join( log_output_path ,'ApiTest_%s.log'%time.strftime('%Y_%m_%d') )
        self.logger = logging.getLogger("ApiTestLog")
        self.logger.setLevel( local_config.LOG_LEVEL )

        console_handler = logging.StreamHandler()  # 控制台输出
        file_handler = logging.FileHandler(self.log_name,'a',encoding='utf-8')  # 文件输出
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler( console_handler )
        self.logger.addHandler( file_handler )

        console_handler.close()  # 防止打印日志重复
        file_handler.close()     # 防止打印日志重复

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()   # 防止打印日志重复

if __name__ == '__main__':
    logger.info('hello')




