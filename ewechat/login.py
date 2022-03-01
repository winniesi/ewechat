import requests
import webbrowser


class Login:
    def __init__(
        self,
        *,
        base_url: str,
        account: str = None,
        password: str = None,
        auth: str = None,
        wid: str = None,
    ) -> None:
        self.base_url = base_url if base_url.endswith("/") else base_url + "/"
        self.account = account
        self.authorization = auth or self._get_authorization(account, password)
        self.wId = wid
        self.wcId = None

    def _make_request(self, *, url_suffix: str, method: str = "post", raw_data: dict):
        """通用请求方法"""
        if self.authorization is None:
            raise Exception("没有登录。")
        url_suffix = url_suffix if not url_suffix.startswith("/") else url_suffix[1:]
        url = self.base_url + url_suffix
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.authorization,
        }
        response = requests.request(method, url, json=raw_data, headers=headers)
        return response

    def _get_authorization(self, account, password):
        """第一步登录账户获取 authorization"""
        url = self.base_url + "member/login"
        response = requests.request(
            "post", url, json={"account": account, "password": password}
        )
        try:
            return response.json().get("data").get("Authorization")
        except Exception:
            raise Exception(response.json())

    def login(self):
        """
        登录微信步骤：
        1. 获取微信二维码
        2. 执行微信登录
        """
        login_params = self.ipad_login()
        self.wId = login_params["wId"]
        qrcode = login_params["qrCodeUrl"]
        print(f"微信扫码登录：{qrcode}")
        webbrowser.open(qrcode)

        self.wcId = self.get_ipad_login_info()["data"]["wcId"]

        if self.wcId and self.wcId:
            with open("logged_in", "w") as file:
                file.write(
                    f"wId={self.wId}\nwcId={self.wcId}\nauthorization={self.authorization}"
                )
            return {
                "wcID": self.wcId,
                "wId": self.wId,
                "authorization": self.authorization,
            }
        else:
            raise Exception("登录失败，请重试。")

    def ipad_login(self):
        """1. 获取微信二维码"""
        raw_data = {"wcId": "", "proxy": "2"}
        response = self._make_request(
            url_suffix="iPadLogin", method="post", raw_data=raw_data
        )
        if response.json()["code"] == "1000":
            return response.json()["data"]
        else:
            raise Exception(response.json())

    def get_ipad_login_info(self):
        """2. 执行微信登录"""
        raw_data = {"wId": self.wId}
        response = self._make_request(url_suffix="getIPadLoginInfo", raw_data=raw_data)
        if response.json()["code"] == "1000":
            return response.json()
        else:
            raise Exception(response.json())

    def is_logged_in(self) -> bool:
        if self.wId is None:
            return False
        try:
            self.get_ipad_login_info()
            return True
        except Exception:
            return False

    def get_my_wcid(self):
        response = self.get_ipad_login_info()
        return response["wcId"]

    def sencond_login(self, saved_wcid: str = None):
        if self.wcId is None and saved_wcid is None:
            raise Exception("需要重新登录，或者通过参数 saved_wcid 传入上次登录后保存的的 wcId")
        wcId = self.wcId or saved_wcid
        raw_data = {"wcId": wcId, "type": 2}
        response = self._make_request(url_suffix="secondLogin", raw_data=raw_data)
        if response.json()["code"] == "1000":
            self.wId = response.json()["data"]["wId"]
            self.wcId = response.json()["data"]["wcId"]
            with open("logged_in", "w") as file:
                file.write(
                    f"wId={self.wId}\nwcId={self.wcId}\nauthorization={self.authorization}"
                )
            return response.json()
        else:
            raise Exception(response.json())

    def _base_request(self, url_suffix: str, **kwargs):
        raw_data = {**kwargs}
        raw_data["wId"] = self.wId
        res = self._make_request(
            url_suffix=url_suffix, method="post", raw_data=raw_data
        ).json()
        if res["code"] == "1000":
            return res["data"]
        else:
            raise Exception(res)
