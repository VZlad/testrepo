# Made for an Android game
#
# Idle Superpowers
#
# I calculated the number of escalations,
# so two specific powers have a probability p
# to show up at the same time in an escalation
# by the time of escalation number n
# n = 2
# 2/(167*166) = c(2,2)*2/(167*166)
# n = 3
# 3*2/(167*166) = c(3,2)*2/(167*166)
# n = 4
# c(4,2)*2/(167*166)
import math


def escalation_number(r):
    p = 0
    n = 0
    while p < r:
        p = p + math.comb(n, 2)*2/(167*166)
        n += 1
    print(p, n)


q = float(input("Enter probability "))
escalation_number(q)
