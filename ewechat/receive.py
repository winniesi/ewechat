from .login import Login


class Receive(Login):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_msg_img(self, msgId: str, content: str, type: int = 1):
        return super()._base_request(
            "getMsgImg", msgId=msgId, content=content, type=type
        )
