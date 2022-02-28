from . import address, send, circle, receive


class Wechat(address.Address, send.Send, circle.Circle, receive.Receive):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
