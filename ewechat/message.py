from .login import Login


class Message(Login):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_text(self, wcId: str, content: str):
        return super()._base_request("sendText", wcId=wcId, content=content)

    def send_file(self, wcId: str, path: str, fileName: str):
        return super()._base_request(
            "sendFile", wcId=wcId, path=path, fileName=fileName
        )

    def send_image(self, wcId: str, content: str):
        return super()._base_request("sendImage2", wcId=wcId, content=content)

    def send_video(self, path: str, thumbPath: str):
        return super()._base_request("sendVideo", path=path, thumbPath=thumbPath)
