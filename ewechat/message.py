from .login import WechatLogin


class WechatMessage(WechatLogin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _base_request(self, url_suffix: str, **kwargs):
        raw_data = {**kwargs}
        raw_data["wId"] = self.wId
        res = (
            super()
            ._make_request(url_suffix=url_suffix, method="post", raw_data=raw_data)
            .json()
        )
        if res["code"] == "1000":
            return res["data"]
        else:
            raise Exception(res)

    def send_text(self, wcId: str, content: str):
        return self._base_request("sendText", wcId=wcId, content=content)

    def send_file(self, wcId: str, path: str, fileName: str):
        return self._base_request("sendFile", wcId=wcId, path=path, fileName=fileName)

    def send_image(self, wcId: str, content: str):
        return self._base_request("sendImage2", wcId=wcId, content=content)

    def send_video(self, path: str, thumbPath: str):
        return self._base_request("sendVideo", path=path, thumbPath=thumbPath)
