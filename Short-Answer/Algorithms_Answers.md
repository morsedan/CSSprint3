#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  
It will run *n* times


b) O(n * log(n))  
The for loop runs *n* times, the while loop runs in O(log(n)) time. So its O(n) * O(log(n))

c) O(n)  
Its pretty much just counting down. Its returning the number of bunnies * 2 so it could be made to be O(1)

## Exercise II

Throw one off the middle floor, if it breaks go to the middle of the floors below you and do the same until you land on one floor. Its a binary search.  
Runtime complexity: O(log(n)), Dividing in half each time

