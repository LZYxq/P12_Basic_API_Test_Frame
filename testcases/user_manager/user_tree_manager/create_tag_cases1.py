# encoding: utf-8
# @author: liusir
# @file: create_tag_cases.py
# @time: 2020/7/5 4:42 下午

import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger

class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        logger.info('[case03] 创建用户标签接口')
        params = {
            'grant_type': 'client_credential',
            'appid': 'wx55614004f367f8ca',
            'secret': '65515b46dd758dfdb09420bb7db2c67f'
        }
        get_access_token_response = self.session.get(url=self.hosts + '/cgi-bin/token',
                             params=params
                             )
        token_id = get_access_token_response.json()['access_token']
        print(token_id)

        get_params = {
            'access_token': token_id
        }
        post_params = '{ "tag" : { "name" : "newdream66655" } }'
        headers = {
            'content_type': 'application/json'
        }
        create_tag_response = self.session.post(url=self.hosts + '/cgi-bin/tags/create',
                              params=get_params,
                              data=post_params,
                              headers=headers
                              )
        actual_result = create_tag_response.json()["tag"]["name"]
        self.assertEqual( actual_result,'newdream66688' )

if __name__=="__main__":
    unittest.main()

