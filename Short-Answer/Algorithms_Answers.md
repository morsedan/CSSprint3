#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) **O(n)** -- because the while loop runs n times because n^3/n^2 = n
```python
def q1(n):
    a = 0
    while a < n * n * n:
        a = a + n * n
'''
n:1 gave a:1 (1 times) in 1.6689300537109375e-06 seconds
n:3 gave a:27 (3 times) in 1.9073486328125e-06 seconds
n:5 gave a:125 (5 times) in 9.5367431640625e-07 seconds
n:100 gave a:1000000 (100 times) in 6.198883056640625e-05 seconds
n:10000 gave a:1000000000000 (10000 times) in 0.0030939579010009766 seconds
n:234535 gave a:12900988463080375 (234535 times) in 0.07631587982177734 seconds
'''
```

b) **O(n log(n))** -- because the outer loop has a O(n) time complexity, and the inside has a O(log n) time complexity because the input gets reduced by a factor each time the loop runs
```python
def q2(n):  # O(nlog(n))
    total = 0
    for i in range(n):  # O(n)
        j = 1
        while j < n:  # O(log(n))
            j *= 2
            total += 1
```

c) **O(n)** -- because it the new input is only being reduced by 1 and not multiplied by anything
```python
def bunny_ears(bunnies):  # O(n+1) -> O(n)
    if bunnies == 0:
        return 0
    return 2 + bunny_ears(bunnies-1)
```
## Exercise II
> Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.
```
recursive function ( highest level to check, lowest level to check ):
    make the checking level (highest level - (lowest level - 1) / 2 + 0.5 -> int)
    if the egg is broken at the checking floor
        check again with recursion from current level to lowest level
    if it is not broken at the checking floor
        check again with recursion from highest level to current level + 1
        
```
