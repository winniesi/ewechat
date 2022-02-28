from .login import Login


class Receive(Login):
    def get_msg_img(self, msgId: str, content: str, type: int = 1):
        return super()._base_request(
            "getMsgImg", msgId=msgId, content=content, type=type
        )
