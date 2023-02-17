"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""


# Use a for loop to check through the string 
# if the string character is not A,E,I,O,U then remove them from the string
# and add them to the new_string
# then return the new_string with zero vowels

def disemvowel(the_string):
    vowels = 'aeiouAEIOU'
    new_string = ""
    # O(n)
    for char in the_string:
        if char not in vowels:
            new_string += char
    return new_string

# Time complexity is O(n)
# it is O(n) because it goes over each letter in the string once
# to check before adding them to the new string
