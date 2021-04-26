# InstaPy "Docs" : https://instapy.org/actions
import os
import sys
import time
import random
from instapy import InstaPy
from instapy import smart_run

# some useless design elements
os.system("title Instagram")
os.system("color c")
print(40*"~", " InstaBot ", 40*"~", "\n\n")
loading = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
         "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

# login input
username = input("           -> username : ")
password = input("           -> password : ")

# loading animation
print(93*"-", "\n")
for i in range(len(loading)):
    time.sleep(0.2)
    sys.stdout.write("\r                                        " + loading[i % len(loading)])
    sys.stdout.flush()
os.system("cls")

# pause
def pause():
    time.sleep(0.2)

# menu
print(40*"¯", " InstaBot ", 40*"¯", "\n\n")
pause()
print("-     unfollow : unfollow")
pause()
print("-     accept follow requests : acceptfollowers")
pause()
print("-     remove follow requests : cancelfollowers")
pause()
print("-     like by hashtag : liketag")
pause()
print("-     follow by hashtag : followtag")
pause()
print("-     follow by followers : followers")
pause()
print("-     follow by following : following")
pause()
print("-     follow by comment : followbycomment")
pause()
print("-     follow by likes : followbylike")
pause()
print("-     follow and like : followlike")
pause()
print("-     follow and comment : followandcomment")
pause()
print("-     follow, like and comment : followlikecomment")
pause()
print("-     follow and comment : followcomment")
pause()
print("-     comment by follower  : commentfollower")
pause()
print("-     comment by following  : commentfollowing")
pause()
print("-     comment by tagged posts  : commenttaggedpost")
pause()
print("-     comment by comments  : commentcomments")
pause()
print("-     comment by likers  : commentliker", "\n\n")
pause()

choise = input("   >>>   How can i help you  : ") # menu picker

if choise == "unfollow":
    print
    setting = session.unfollow_users(amount=)
