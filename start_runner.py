#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: start_runner.py
# @time: 2020/7/5 5:05 下午
import unittest
from common import HTMLTestReportCN
from common.localconfig_utils import local_config
from common.email_utils import EmailUtils

def get_all_cases_suite():
    discover = unittest.defaultTestLoader.discover(
                            start_dir='./testcases',
                            pattern='*_cases.py',
                            top_level_dir='./testcases'
                        )
    all_cases_suite = unittest.TestSuite()
    all_cases_suite.addTest( discover )
    return all_cases_suite

report_dir = HTMLTestReportCN.ReportDirectory( local_config.REPORT_PATH + '/' )
report_dir.create_dir('API_TEST_')
# dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open( report_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         tester="liuzhongyi",
                                         title="OM_API_TEST",
                                         description="study~~~")
runner.run( get_all_cases_suite() )
fp.close()
# EmailUtils( open(report_path,'rb').read() ,report_path).send_mail()
if __name__=='__main__':
    # get_all_cases_suite()
    # report_path = RunCase().run()
    EmailUtils( open(report_path,'rb').read(),report_path).send_mail()

