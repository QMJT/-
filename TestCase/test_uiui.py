import allure
import pytest

from Common import Request, Assert, read_excel, Login

request = Request.Request()
assertinons = Assert.Assertions()

ids_list = []

tyh_id = 0
hede = Login.Login().get_token()
url = 'http://192.168.60.132:8080/'

excel_list = read_excel.read_excel_list('./document/退货.xlsx')

for i in range(len(excel_list)):
    ids_pop = excel_list[i].pop()

    ids_list.append(ids_pop)


@allure.feature('退货接口')
class Test_Return_goods:

    @allure.story('退货列表')
    def test_Coupon_in(self):
        in_if = request.get_request(url=url + 'returnReason/list', params={'?pageNum': 1, 'pageSize': 5},
                                    headers=hede)
        assertinons.assert_code(in_if.status_code, 200)
        in_if_json = in_if.json()
        assertinons.assert_in_text(in_if_json['message'], '成功')
        data_json = in_if_json['data']
        list_json = data_json['list']
        item = list_json[0]
        global tyh_id
        tyh_id = item['id']

    @allure.story('删除退货')
    def test_delete_to(self):
        delete_in = request.post_request(url=url + 'returnReason/delete', params={'ids': tyh_id},headers=hede)
        assertinons.assert_code(delete_in.status_code, 200)
        delete_if_json = delete_in.json()
        assertinons.assert_in_text(delete_if_json['message'], '成功')

    @allure.story('添加退货原因')
    @pytest.mark.parametrize('name,sort,status,msg', excel_list, ids=ids_list)
    def test_add_to(self, name, sort, status, msg):
        add_in = request.post_request(url=url + 'returnReason/create',
                                      json={"name": name, "sort": sort, "status": status, "createTime": ''},
                                      headers=hede)
        assertinons.assert_code(add_in.status_code, 200)
        add_if_json = add_in.json()
        assertinons.assert_in_text(add_if_json['message'], msg)