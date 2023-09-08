'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th_loops(word):

    word_arr = list(word)
    th_count = 0

    if not word_arr:
        return th_count

    for i in range(len(word_arr)):

        if word_arr[i] == 't' and i+1 != len(word_arr) and word_arr[i+1] == 'h':
            th_count += 1
    
    return th_count

def count_th(word, th_count=0):
    
    if not word or len(word) == 1:
        return th_count
    
    if (list(word)[0] == 't' and list(word)[1] == 'h'):
        return count_th(word[1:], th_count+1)
    
    return count_th(word[1:], th_count)
