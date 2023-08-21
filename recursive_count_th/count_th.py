"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

"""
# check for lowercase t's, if next character is a h then add to count -- requires loops, don't use
Check first two character for "th"
return 1 + repeat (starting +=1...end) -- if true
return repeat (starting +=1...end) -- if false
"""


def count_th(word):
    if len(word) < 2:
        return 0
    if word[0:2] == "th":
        return 1 + count_th(word[1:len(word)])
    return 0 + count_th(word[1:len(word)])
