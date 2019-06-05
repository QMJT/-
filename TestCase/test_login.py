import allure
import pytest

from Common import Request,Assert,read_excel


#调用模块里的方法  取个别名
ruquest=Request.Request()
#调用模块里的方法  取个别名
assertinons=Assert.Assertions()
#  用例的路径
excel_list = read_excel.read_excel_list('./document/test.xlsx')
#建一个空的list 用于调出来存储
ids_list=[]
#用长度遍历 遍历每一个 附到i集合里
for i in range (len(excel_list)):
#查询i 删除 最后一个取一个变量名

    ids_pop=excel_list[i].pop()
#把删除的存到新的变量里
    ids_list.append(ids_pop)

@allure.feature('登录模块')
class Test_login:


    # @allure.story('登录')
    # def test_login(self):
    #     login_resp=ruquest.post_request(url='http://192.168.60.132:8080/admin/login',
    #                                 json={"username": "admin", "password": "123456"})
    #
    #     assertinons.assert_code(login_resp.status_code,200)
    #     print(login_resp.text)
    #
    #     print(type(login_resp.text))
    #
    #     login_resp_json=login_resp.json()
    #
    #     print(type(login_resp_json))
    #
    #     assertinons.assert_in_text(login_resp_json['message'])





    @allure.story('登录参数化')
    @pytest.mark.parametrize('name,pwd,msg',excel_list,ids=ids_list)
    def test_login(self,name,pwd,msg):
        login_resp = ruquest.post_request(url='http://192.168.60.132:8080/admin/login',
                                          json={"username": name, "password": pwd})

        assertinons.assert_code(login_resp.status_code, 200)
        print(login_resp.text)

        print(type(login_resp.text))

        login_resp_json = login_resp.json()

        print(type(login_resp_json))

        assertinons.assert_in_text(login_resp_json['message'],msg)



