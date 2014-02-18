#ext
import urllib2
import json
import matplotlib.pyplot as plt
#import numpy

#int


# Creating JSON
count = 100
req = "http://zumic.com/?json=get_recent_posts&count=" + str(count)
posts_json = urllib2.urlopen(req).read()
json_out = open("recent_posts.json", "w")
json_out.write(posts_json)
json_out.close() # always be closing!!
print("Wrote to recent_posts.json")


# Parsing JSON data
# http://zumic.com/?json=get_recent_posts&count=100
# ^ can also replace "get_recent_posts" with "get_posts&orderby=date"

#d_raw = open("recent_posts.json", "r").read()
d_raw = posts_json # also works and bypasses file opening
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
print("Wrote to post_titles.csv")
dates_out.write("\n".join(post_dates))
print("Wrote to post_dates.csv")


# 
# numpy.savetxt("titles.csv", post_titles, delimiter=",")
# numpy.savetxt("dates.csv", post_dates, delimiter=",")

# plt.plot(post["date"])
# plt.ylabel('some numbers')
# plt.show()



# https://clicky.com/stats/api4?site_id=100591291&date=last-30-days&filter=&sitekey=46a8d7ed022b30ce&type=pages&output=js&&limit=100&page=1