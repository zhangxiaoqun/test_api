# -*- coding: utf-8 -*-
# @Time : 2021/4/23 16:53
# @File : conftest2.py
# @Software: PyCharm


import time
from Crm_login.Login import get_token
from CRM_interface.field import Platform_api  as Pm
from configs.config import CODE_PAW  #无码账号


# # 删除文件夹
# def del_Folder( token):
#     url = f'{host}/app/api/v1/app/packages/{fileId_List[2]}'
#     # url = f'{host}/app/api/v1/app/packages/{Platform_api().list_packages(token)[0][0]}'
#     user_Token = {'Authorization': token}
#     res = requests.delete(url, headers=user_Token)
#     return res.json()  ##{'success': True, 'message': '成功', 'code': 0, 'data': None, 'timestamp': 1616480671171}
#
#
# # 删除数据表
# def del_dataTable(token):
#     url = f'{host}/app/api/v1/apps/{formID_List[2]}'
#     # url = f'{host}/app/api/v1/apps/{Platform_api().list_packages(token)[1][0]}'
#     user_Token = {'Authorization': token}
#     res = requests.delete(url, headers=user_Token)
#     return res.json()  # {'success': True, 'message': 'OK', 'code': 0, 'data': True, 'timestamp': 1616481442113}



#本地时间
localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#登录
token = get_token(CODE_PAW)
P = Pm()


# @pytest.fixture(scope='module', autouse=True)  # 环境初始化 、数据清除
# def delete_all_(request):
#     formId_list = P.list_packages(token)[0]
#     fileID_list = P.list_packages(token)[1]
#
#
#     for formID in formId_list:
#         P.del_dataTable(token , formID)
#         print("正在删除表单")
#     for flieID in fileID_list:
#         P.del_Folder(token , flieID)
#         print("正在删除文件夹")
#
#
#
#     for one in range(10):
#         res = P.add_newFolder(token)
#         file_ID = res['data']['id']
#         P.add_dataTable(token , file_ID , f'文件夹{one}' )
#         print('正在新增文件夹和表单')
#     # 环境、数据清除----teardown
#     def fin():
#
#         print('----测试环境恢复----')
#
#     request.addfinalizer(fin)
#

if __name__ == "__main__":
    formId_list = P.list_packages(token)[1]
    fileID_list = P.get_fileID(token)
    # print(fileID_list)


    for formID in formId_list:
        P.del_dataTable(token , formID)
        print("正在删除表单")
    for flieID in fileID_list:
        P.del_Folder(token , flieID)
        print("正在删除文件夹")


    for one in range(10):
        res = P.add_newFolder(token , f'文件夹{one}' )
        file_ID = res['data']['id']
        print(file_ID)
        P.add_dataTable(token , file_ID , f'表单{one}' )
        print('正在新增文件夹和表单')