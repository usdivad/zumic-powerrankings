import json
import matplotlib.pyplot as plt
#http://zumic.com/?json=get_recent_posts&count=50
d_raw = open("./recent_posts.json").read()
data = json.loads(d_raw)["posts"]

for post in data:
    print(post["title"] + ": " + post["date"])
    
    
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()