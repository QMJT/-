import allure
import pytest

from Common import Request,Assert,read_excel
excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
ids_list=[]
heders={}
yhq_id=0

for i in range(len(excel_list)):
    # 查询i 删除 最后一个取一个变量名

    ids_pop = excel_list[i].pop()
    # 把删除的存到新的变量里
    ids_list.append(ids_pop)

request=Request.Request()
assertinons=Assert.Assertions()



@allure.feature('商品优惠券')
class Test_Coupon_info:

    @allure.story('登录接口')
    def test_iogin(self):
        login_resp = request.post_request(url='http://192.168.60.132:8080/admin/login',
                                          json={"username": "admin", "password": "123456"})
        assertinons.assert_code(login_resp.status_code, 200)
        login_resp_json = login_resp.json()
        assertinons.assert_in_text(login_resp_json['message'], '成功')

        # 提取token
        data_json = login_resp_json['data']
        token = data_json['tokenHead'] + data_json['token']

        # 重新赋值全局变量
        global hede
        hede = {'Authorization': token}

    @allure.story('优惠券列表')
    def tsst_list(self):
        list_info=request.get_request(url='http://192.168.60.132:8080/coupon/list',
                            params={'pageNum':1,'pageSize':10},heders=hede)
        assertinons.assert_code(list_info.status_code, 200)
        list_info_json = list_info.json()
        assertinons.assert_in_text(list_info_json['message'], '成功')



    @allure.story('查询接口')
    def sete_query(self):
        query_info = request.get_request(url='http://192.168.60.132:8080/coupon/list',
                                          params={'pageNum': 1, 'pageSize': 10, }, heders=hede)
        assertinons.assert_code(query_info.status_code, 200)
        query_info_json = query_info.json()
        assertinons.assert_in_text(query_info_json['message'], '成功')
        #先提出来给 他一个变量名
        data_json = query_info_json['data']
        #变量名 来提取下一个  在给他个变量名
        list_json = data_json['list']
        dan = list_json[0]
        #global 重新赋值全局变量
        global yhq_id
        yhq_id = dan['id']

    @allure.story('删除优惠券')
    def sete_delete(self):
        delete_info = request.post_request(url='http://192.168.60.132:8080/coupon/delete/' + str(yhq_id))
        assertinons.assert_code(delete_info.status_code, 200)
        delete_json = delete_info.json()
        assertinons.assert_in_text(delete_json['message'], '成功')




    @allure.story('优惠券添加')
    @pytest.mark.parametrize('name,amount,minPoint,publishCount,msg', excel_list, ids=ids_list)
    def sete_add_to(self,name,amount,minPoint,publishCount,msg):
        add_to=request.post_request(url='http://192.168.60.132:8080/coupon/create',
                             json={"type":0,"name":name,"platform":0,"amount":amount,"perLimit":1,"minPoint":minPoint,
                                   "startTime":'',"endTime":'',"useType":0,"note":'',"publishCount":15,
                                   "productRelationList":publishCount,"productCategoryRelationList":[]},heders=hede)
        assertinons.assert_code(add_to.status_code, 200)
        add_to_json = add_to.json()
        assertinons.assert_in_text(add_to_json['message'], msg)

