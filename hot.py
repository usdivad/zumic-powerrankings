# http://www.evanmiller.org/rank-hotness-with-newtons-law-of-cooling.html
# http://amix.dk/blog/post/19574

import math
COOLING_RATE = 0.05
BASE = 3
GRAVITY = 0.5
OFFSET = 24

#Paul Graham's HN hotness algorithm
def hn_score(score, age_hours, gravity=GRAVITY, offset_hours=OFFSET):
    if age_hours >= offset_hours:
        #return (score-1)/pow((age_hours+2), gravity) #HN verbatim
        return score/pow(age_hours-offset_hours, gravity)
    else:
        return score

#Newtonian cooling function, modified
def newton_score(temperature, hours):
    if hours >= OFFSET:
        #return temperature * math.exp(-(COOLING_RATE) * hours)
        return temperature * pow(BASE, (-(COOLING_RATE) * hours))
    else:
        return temperature

#Calc score to be fed into decay algs
def pre_decay_score(popularity, grade):
    return popularity*grade
    
base = 1000
elapsed = 36
print "newton_score: " + str(newton_score(base, elapsed))
print "hn_score: " + str(hn_score(base, elapsed))


# Excel fns:
# newton_score: =IF(F2>24, C2*POWER($A$6,(-$A$3*F2)), C2)
# hn_score: =IF(F2>24, C2/POWER(F2-23,$A$12), C2)
# ^Note for the above that C2 = popularity * grade

# Todo:
# - keep tweaking pre_decay
# - get attrs (views, likes, grade) from zumic posts
# - use numpy, matplotlib to graph in python