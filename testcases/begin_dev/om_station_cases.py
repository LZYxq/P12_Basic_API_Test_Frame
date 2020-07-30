import requests
import unittest
from common.localconfig_utils import local_config
from common.log_utils import logger
import warnings
from testcases.begin_dev.om_login_cases import OM_login


class station(unittest.TestCase):
    # OM_login.setUp()
    # OM_login.tearDown()
     # OM_login.test_asset_token()
     # access_token = {}
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.hosts = local_config.URL
        self.session = requests.session()
        self.headers = {
            'Authorization': 'Bearer ' + OM_login.access_token['access_token'],
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Accept': 'application/json, text/plain, */*'
        }

    def tearDown(self) -> None:
        pass

    def test_get_stationall(self):
        """[case04]获取所有站点"""
        logger.info('获取所有站点')
        params={
            'size':1000,
            'current':1,
            'sort':1
        }
        # respose =OM_login.session.get(url=self.hosts + '/apis/om/station/all',headers=self.headers,params=params)
        respose=self.session.get(url=self.hosts+'/apis/om/station/all',headers=self.headers,params=params)
        logger.info(print(respose.text))
        self.assertEquals(respose.text ['code'] ,'0')

    def test_get_stattionallstatus(self):
        """[case05]获取所有站点状态"""
        respose=self.session.get(url=self.hosts +'/apis/om/alarm/selectAllStationStatus',headers=self.headers)

        print(respose.json())
        # self.assertEqual(respose, '4')


    def test_get_alarmselectAlarmList(self):
        """[case06]获取所有报警列表"""
        params={
            'cuurent':1,
            'size':10000
        }
        respose=self.session.get(url=self.hosts+'/apis/apis/om/alarm/selectAlarmList',headers=self.headers,params=params)
        print(respose.text)

    def test_get_apisomworkorder(self):
        """[case07]获取所有工单"""
        params={
            'current':1,
            'size':10000
        }
        respose=self.session.get(url=self.hosts+'/apis/om/workorder/page',headers=self.headers,params=params)
        print(respose.text)


    def test_om_stationSID(self):
        """[case08]进入站点的sid图"""
        respose=self.session.get(url=self.hosts+'/apis/om/station/order/1245597104693436417',headers=self.headers)
        print(respose.text)

    def test_selectAlarmHistory(self):
        """[case09]查询所有报警的历史数据"""
        params={
            'current':1,
            'size':10,
            'endTimeSort':0,
            'stationId':''
        }
        respose=self.session.get(url=self.hosts+'/apis/om/alarmhistory/selectAlarmHistory',headers=self.headers,params=params)
        print(respose.text)


    def test_omcheckdata(self):
        """[case10]检查站点数据"""
        params={
            'current':'1',
            'size':'100000'
        }
        respose=self.session.get(url=self.hosts+'/apis/om/checkdata/page',headers=self.headers,params=params)
        print(respose.text)

    def test_findworkorder(self):
        """[case11]查询工单"""
        params={
            'current':'1',
            'size':'10',
            'orderField':'createTime',
            'orderType':'desc',
            'status':'',
            'title':'',
            'startTime':'',
            'endTime':''
        }
        respose=self.session.get(url=self.hosts+'/apis/om/workorder/page',headers=self.headers,params=params)
        print(respose.text)

    def test_asset(self):
        """[case12]查询站点的资产"""
        params={
            'current':'1',
            'size':'10000'
        }
        respose=self.session.get(url=self.hosts+'/apis/om/asset/type/1245546284471840769?',headers=self.headers,params=params)
        print(respose.text)

    def test_deviceallpsrsm(self):
        """[case13]获取站点的参数"""
        params={
            'deviceId':'1245546654031966210',
            'current':'1',
            'size':'10000'
        }
        respose=self.session.get(url=self.hosts+'/apis/om/device/allParamByDeviceId?',params=params,headers=self.headers)
        print(respose.text)

    def test_get_thinsboardtoken(self):
        """[case14]获取thinsboard的token"""
        respose=self.session.get('http://xre.tpddns.cn:8086'+'/apis/om/thingsboard/getToken',headers=self.headers)
        print(respose.text)



if __name__=="__main__":
    unittest.main()