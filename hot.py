# http://www.evanmiller.org/rank-hotness-with-newtons-law-of-cooling.html
# http://amix.dk/blog/post/19574

import math
COOLING_RATE = 0.05
GRAVITY = 0.5
OFFSET = 24

def hn_score(score, age_hours, gravity=GRAVITY, offset_hours=OFFSET):
    if age_hours >= offset_hours:
        #return (score-1)/pow((age_hours+2), gravity) #HN verbatim
        return score/pow(age_hours-offset_hours, gravity)
    else:
        return score

def decay(temperature, hours):
    return temperature * math.exp(-(COOLING_RATE) * hours)
    
base = 1000
elapsed = 36
print "decay: " + str(decay(base, elapsed))
print "hn_score: " + str(hn_score(base, elapsed))