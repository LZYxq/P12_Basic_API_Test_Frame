
import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger
import  warnings


class OM_login(unittest.TestCase):
    access_token = {}
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)
        self.hosts = local_config.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_getom(self):
        """[case01] 正常获取进入om登录页测试"""
        logger.info('[case01] 正常获取om登录页测试')
        headers={
            'content_type': 'application/json'
        }
        actual_result = self.session.get(url=self.hosts + '/login',headers=headers)

        print(actual_result)
        # self.assertEqual(actual_result.json()['expires_in'], 7200)

    def test_asset_token(self):
        """[case02]获取用户的token"""
        logger.info('[case02]获取用户的登录token')
        # post_params = '{ "tag" : { "name" : "newdream66655" } }'
        data = {
                "username": "admin",
                "password": "123456",
                "scope": "server",
                "grant_type": "password"
        }
        headers = {
            'content_type': 'application/x-www-form-urlencoded',
            'Accept': 'application / json, text / plain, * / *',
            'User - Agent':  'Mozilla / 5.0(Windows NT 10.0; Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 83.0.4103.116Safari / 537.36',
            'Authorization': 'Basic dGVzdDp0ZXN0',
            'Connection': 'keep-alive',
            'content_type': 'application/json'
        }
        actual_result = self.session.post(url=self.hosts + '/apis/auth/oauth/token',
                                          headers=headers,
                                          data=data
                                          )

        # print(actual_result.text)

        OM_login().access_token['access_token']= actual_result.json()['access_token']
        print(OM_login.access_token['access_token'])
        refresh_token = actual_result.json()['refresh_token']
        # print(access_token)
        print(refresh_token)


        # self.assertEqual(actual_result.json()['expires_in'], 36577)

    def test_get_user_info(self):
        """[case03]获取用户信息"""
        logger.info('[case01] 正常获取用户信息测试')

        headers ={
            'content_type': 'application/json',
            'Authorization':'Bearer'+ OM_login.access_token['access_token']
        }
        actual_result = self.session.get(url=self.hosts + '/admin/user/info',headers=headers)
        logger.info('请求用户数据')
        print(actual_result.content.decode('utf-8'))

OM_login=OM_login()
if __name__=="__main__":
    # suite=unittest.TestSuite()
    # suite.addTest(OM_login('test_asset_token'))
    unittest.main()
