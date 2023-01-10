class Post:
    def __init__(self, username, user_id, media, \
                 avatar, comment_button, caption, likes, comments, like_button):
        self.username = username
        self.user_id = user_id
        self.media = media
        self.avatar = avatar
        self.comment_button = comment_button
        self.caption = caption
        self.likes = likes
        self.comments = comments
        self.like_button = like_button

username = "ello govna, top o' the mornin' to ya!"
user_id = 112010
media = "img/photogram/waterfall.png"
avatar = "img/photogram/avatar_icon.png"
comment_button = "img/photogram/add_comment.png"
caption = "First time at Yosemite. It has surpassed all of my expectations."
likes = 23
comments = ["Beautiful!", "I wish I was there too.", "Is that Nevada Falls?", "Love it!", "Can't wait for the Halfdome pictures", "More pics please"]
like_button = "img/photogram/likes_icon.png"

post1 = Post(username, user_id, media, avatar, comment_button, caption, likes, comments, like_button)


