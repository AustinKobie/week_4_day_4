"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""
# Make an empty array to contain names that can be entered
# create if staements for each amount up to 3
# Make an if statement for the amount of names being entered caping at 4 before
# being turned into a integer value
# call the arrays with a f strings to get the array to print with the strings 

# O(1) Time Complexity 
def likes(names):
    num_likes = len(names)
    # O(1)
    if num_likes == 0:
        return 'no one likes this'
    # O(1)
    elif num_likes == 1:
        return f'{names[0]} likes this'
    # O(1)
    elif num_likes == 2:
        return f'{names[0]} and {names[1]} like this'
    # O(1)
    elif num_likes == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    # O(1)
    else:
        return f'{names[0]}, {names[1]} and {num_likes - 2} others like this'

    
print(likes(['Max', 'John', 'Mark']))
        
#  This is O(1) time complexity because the function gets O(1) from the len function
#  we use elifs through out to determin the output based on the lenght of the list
#  even if we have more then three names it still only preforms a dixed amount of operations 
