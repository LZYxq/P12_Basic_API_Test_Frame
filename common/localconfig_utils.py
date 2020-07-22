#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: localconfig_utils.py
# @time: 2020/7/5 11:58 上午

import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join( current_path , '..' ,'config/config.ini' )


class LocalconfigUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding='utf-8')

    @property   #把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default','URL')
        return url_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path','LOG_PATH')
        return log_path_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('path','REPORT_PATH')
        return report_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int( self.cfg.get('log','LOG_LEVEL') )
        return log_level_value

    @property
    def CASE_PATH(self):
        case_path_value = self.cfg.get('path', 'CASE_PATH')
        return case_path_value

    @property
    def SMTP_SERVER(self):
        smtp_server_value = self.cfg.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def SMTP_SENDER(self):
        smtp_sender_value = self.cfg.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def SMTP_PASSWORD(self):
        smtp_password_value = self.cfg.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def SMTP_CC(self):
        smtp_cc_value = self.cfg.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def SMTP_SUBJECT(self):
        smtp_subject_value = self.cfg.get('email', 'smtp_subject')
        return smtp_subject_value


local_config = LocalconfigUtils()

if __name__=="__main__":
    print( local_config.REPORT_PATH )  #config.URL()