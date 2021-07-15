import pytest
import requests
import os
import allure

@allure.feature("测试Demo")
class TestClass:
    def getParame(self):
        # 两种传参方式
        # 1.字符串拼接
        response = requests.get(
            url="https://api.binstd.com/train/station2s?start=北京&end=西安&ishigh=0&appkey=d737aad9a0d9dc97")
        # 字符串格式
        print(response.text)
        # json格式，要保证返回的格式是json
        print(response.json())


        # 2.字典方式
        _url = "https://api.binstd.com/train/station2s"
        _params = {
            "start" : "北京",
            "end" : "西安",
            "ishigh" : 0,
            "appkey" : "d737aad9a0d9dc97"

        }
        response2 = requests.post(url = _url,params = _params)
        # 字符串格式
        print(response2.text)
        # json格式，要保证返回的格式是json
        print(response2.json())
        # 响应状态码
        print(response2.status_code)
        # 获取原始模式
        print(response2.raw)
        return  response2

    # 始发站测试
    # @pytest.mark.run
    @allure.story("测试用例1")
    def test_station_endstation(self):
        # 获取返回的车站数据列表
        trainList = self.getParame().json()["result"]["list"]

        # 循环列表，判断北京到西安是否在列表中
        for train in trainList:
            assert "北京" in train["station"]
            assert "西安" in train["endstation"]

    # 测试用例2
    @allure.story("测试用例2")
    def test_demo2(self):
        x = "hello"
        assert "d" in x

if __name__ == "__main__":
    pytest.main(["-sq","--alluredir","../../report/allure_raw"])
    os.system("allure generate ../../report/allure_raw -o ../../report/allure_report --clean")