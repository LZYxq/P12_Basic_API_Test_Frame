#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: get_access_token_cases.py
# @time: 2020/7/5 4:41 下午

import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger

class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        """[case01] 正常获取access_token值测试"""
        logger.info('[case01] 正常获取access_token值测试')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wx55614004f367f8ca',
            'secret': '65515b46dd758dfdb09420bb7db2c67f'
        }
        actual_result = self.session.get(url=self.hosts + '/cgi-bin/token',
                             params=params
                             )
        self.assertEqual(actual_result.json()['expires_in'],7200)

    def test_appid_error(self):
        self._testMethodDoc = '[case02] appid错误时测试'
        logger.info('[case02] appid错误时测试')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wx55614004f367f8',
            'secret': '65515b46dd758dfdb09420bb7db2c67f'
        }
        actual_result = self.session.get(url=self.hosts + '/cgi-bin/token',
                             params=params
                             )
        self.assertEqual(actual_result.json()['errcode'],40013)

if __name__=="__main__":
    unittest.main()
