from .login import Login


class Receive(Login):
    def get_msg_img(self, msgId: str, content: str, type: int = 1):
        """下载图片"""
        return super()._base_request(
            "getMsgImg", msgId=msgId, content=content, type=type
        )

    def set_http_callback_url(self, httpUrl: str, type: int):
        """设置消息接收地址
        :param type: 1:原生版 2:优化版
        """
        return super()._base_request("setHttpCallbackUrl", httpUrl=httpUrl, type=type)

    def cancel_http_callback_url(self):
        """取消消息接收"""
        return super()._base_request("cancelHttpCallbackUrl")
