import itertools

def imright(h1,h2):
    "House h1 is immediately right of h2 if h1-h2 == 1."
    return h1-h2 == 1

def nextto(h1, h2):
    "Two houses are next to each other if they differ by 1."
    return abs(h1-h2) == 1

def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA) indicating their house numbers."
    houses = first, _, middle, _, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  #1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)              #6
                for (Englishman, Spaniard, Ukrain, Japanese, Norwegian) in orderings
                if Englishman is red                  #2
                if Norwegian is first                 #10
                if nextto(Norwegian, blue)            #15
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog                    #3
                if OldGold is snails                  #7
                if nextto(Chesterfields, fox)         #11
                if nextto(Kools, horse)               #12
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green                    #4
                if Ukrain is tea                      #5
                if milk is middle                     #9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow                    #8
                if LuckyStrike is oj                  #13
                if Japanese is Parliaments            #14
                )

import time

def timecall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)



