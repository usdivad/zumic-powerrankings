#ext
import json
import matplotlib.pyplot as plt
#import numpy

#int


#Parsing JSON data
#http://zumic.com/?json=get_recent_posts&count=50
d_raw = open("./recent_posts.json").read()
data = json.loads(d_raw)["posts"]
post_titles = []
post_dates = []
titles_out = open("post_titles.csv", "w")
dates_out = open("post_dates.csv", "w")

for post in data:
    #print(post["title"] + ": " + post["date"])
    post_titles.append(post["title"])
    post_dates.append(post["date"])
    

class post(object):
    def __init__(self, p):
        self.title = p["title"]
        self.date = p["date"]
        
        
titles_out.write("\n".join(post_titles))
dates_out.write("\n".join(post_dates))


# 
# numpy.savetxt("titles.csv", post_titles, delimiter=",")
# numpy.savetxt("dates.csv", post_dates, delimiter=",")

# plt.plot(post["date"])
# plt.ylabel('some numbers')
# plt.show()