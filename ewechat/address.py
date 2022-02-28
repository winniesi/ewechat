from .login import Login
import sys


class Address(Login):
    def init_address_list(self, wId):
        """初始化通讯录列表，获取通讯录列表之前必须调用此接口。"""
        sys.stdout.write("初始化通讯录列表，时间较长，请耐心等待...\n")
        return super()._base_request("initAddressList", wId=wId)

    def get_address_list(self, wId):
        """获取通讯录列表"""
        return super()._base_request("getAddressList", wId=wId)

    def get_contact(self, wId, wcId):
        """获取联系人信息"""
        return super()._base_request("getContact", wId=wId, wcId=wcId)
