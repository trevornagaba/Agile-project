""" Class that contains models needed in our application"""
class Comments:
    def __init__(self, comment_id, body, author):
        self.body = body
        self.author = author
        self.comment_id = comment_id