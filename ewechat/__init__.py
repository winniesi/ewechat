from . import message, circle


class Wechat(message.Message, circle.Circle):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
