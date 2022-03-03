from .login import Login


class Circle(Login):
    def get_friend_circle(self, wcId: str, firstPageMd5: str = "", maxId: int = 0):
        """获取指定好友的朋友圈"""
        return super()._base_request(
            "getFriendCircle", wcId=wcId, firstPageMd5=firstPageMd5, maxId=maxId
        )

    def sns_send(self, content: str):
        """发送文字朋友圈"""
        return super()._base_request("snsSend", content=content)

    def sns_send_image(
        self, content: str, paths: str, groupUser: str = None, blackList: str = None
    ):
        """发送图片朋友圈图片
        :param content: 文本内容
        :param paths: 图片url（多个用;分隔 单张图片最大3M以内）
        :param groupUser: 对谁可见（传微信id,多个用,分隔）
        :param blackList: 对谁不可见（传微信id,多个用,分隔）
        """
        return super()._base_request(
            "snsSendImage",
            content=content,
            paths=paths,
            groupUser=groupUser,
            blackList=blackList,
        )
