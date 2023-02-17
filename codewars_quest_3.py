"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.   
"""
# This problem is going to take the input from the user
# we are going to go take our number and check 
# if the number has mulitples of 3 or 5 below it 
# take all of those numbers and we are going to add them together
# and finaly return the sum
# O(n) time complexity
def solution(number):
    multiple = []
    # O(n)
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            multiple.append(i)
    return sum(multiple)

# This is O(n) time complexity because the 
# for loop only goes until it reaches it set number
# meaning it should only loop once through the list

    