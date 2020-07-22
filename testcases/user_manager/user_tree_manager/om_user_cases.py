import unittest
import requests
import re
from common.localconfig_utils import local_config
from common.log_utils import logger
import warnings
from testcases.begin_dev.om_login_cases import OM_login


class user_manager(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.hosts = local_config.URL
        self.session = requests.session()
        pass

    def tearDown(self) -> None:
        pass

    def test_findallMenber(self):
        """[case user01]获取所有成员信息"""
        logger.info('获取om的所有用户信息')
        headers = {
             'Authorization': 'Bearer ' + OM_login.access_token['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        params = {
            'size': 10,
            'current': 1,
            'orderBy':'createTime',
            'username':''
        }
        respose=self.session.get(url=self.hosts+'/apis/admin/user/page',headers=headers,params=params)
        print(respose.text)

    def test_getRole(self):
        """[case user01]获取所有角色信息"""
        logger.info('获取om的所有角色信息')
        headers = {
            'Authorization': 'Bearer ' + OM_login.access_token['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        params = {
            'size': 10,
            'current': 1,
        }
        respose = self.session.get(url=self.hosts + '/apis/admin/role/list', headers=headers, params=params)
        print(respose.text)

    def test_greatemember(self):
        """[case user01]创建用户"""
        logger.info('创建用户')
        headers = {
            'Authorization': 'Bearer ' + OM_login.access_token['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        params = {"trelloName":"","username":"fff","sex":"0","role":[2],"phone":"15552115654","email":"23@qq.com","password":"123456","birthDate":"2020-07-22","staffNumber":"","deptId":1,"deptName":"","lockFlag":"0","$lockFlag":"有效"}

        respose= self.session.get(url=self.hosts+'/apis/admin/user',headers=headers,data=params)
        print(respose.text)

    def test_tree(self):
        """[]查询所有的菜单权限管理"""
        headers = {
            'Authorization': 'Bearer ' + OM_login.access_token['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }
        respose=self.session.get(url=self.hosts+'/apis/admin/menu/tree',headers=headers)
        print(respose.text)




