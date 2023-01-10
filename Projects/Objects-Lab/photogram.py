import Post
import tkinter

username = "Preston_Frye13"
user_id = 112010
media = "img/photogram/waterfall.png"
avatar = "img/photogram/avatar_icon.png"
comment_button = "img/photogram/add_comment.png"
caption = "First time at Yosemite. It has surpassed all of my expectations."
likes = 23
comments = ["Beautiful!", "I wish I was there too.", "Is that Nevada Falls?", "Love it!",
                "Can't wait for the Halfdome pictures", "More pics please"]
like_button = "img/photogram/likes_icon.png"

post1 = Post.Post(username, user_id, media, avatar, comment_button, caption, likes, comments, like_button)

window = tkinter.Tk()
window.title("Photogram")
window.geometry("800x500")
window.configure(background="white")

window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=1)

photo = tkinter.PhotoImage(file=post1.media)
comment_button = tkinter.PhotoImage(file=post1.comment_button)
avatar = tkinter.PhotoImage(file=post1.avatar)
like_button = tkinter.PhotoImage(file=post1.like_button)

image = tkinter.Label(
    window,
    image=photo,
    bg="white")

image.grid(
    row=0,
    column=0,
    rowspan=10,
    stick="W")

user_avatar = tkinter.Label(
    window,
    image=avatar,
    width=30,
    bg="white")

user_avatar.grid(
    row=0,
    column=1,
    sticky="W")

user_name = tkinter.Label(
    window,
    text=post1.username,
    font="DejaVuSans 14 bold",
    justify="left",
    bg="white")

user_name.grid(
    row=0,
    column=2,
    sticky="W")
window.mainloop()
