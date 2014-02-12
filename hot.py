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
    
base = 1000
elapsed = 36
print "newton_score: " + str(newton_score(base, elapsed))
print "hn_score: " + str(hn_score(base, elapsed))