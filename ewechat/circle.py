from .login import Login


class Circle(Login):
    def get_friend_circle(self, wcId: str, firstPageMd5: str = "", maxId: int = 0):
        """获取指定好友的朋友圈"""
        return super()._base_request(
            "getFriendCircle", wcId=wcId, firstPageMd5=firstPageMd5, maxId=maxId
        )
