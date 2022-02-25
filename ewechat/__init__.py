from . import send, circle, receive


class Wechat(send.Send, circle.Circle, receive.Receive):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
