# import pytest
# import allure
# import os
#
# @allure.feature("测试Demo2")
# class TestDemo2:
#
#     # 用例1
#     @allure.story("用例1")
#     def test_one(self):
#         x = 10
#         assert 3 == x
#
#     # 用例2
#     @allure.story("用例2")
#     def test_two(self):
#         x = "hello"
#         assert "h" in x
#
#     # 用例3
#     @allure.story("用例3")
#     def test_three(self):
#         x = 10
#         assert 20 > x
#
# if __name__ == "__main__":
#     pytest.main(["-sq","--alluredir","../../report/allure_raw"])
#     os.system("allure generate ../../report/allure_raw -o ../../report/allure_report --clean")
