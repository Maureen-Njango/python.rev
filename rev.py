#/Write a program that calculates the average of three numbers. The user should be prompted to enter the three numbers.

def calculate_average(num1,num2,num3):
    average = (num1 +num2 + num3)/3
    
    print(average) 
#Write a program that calculates the factorial of a number. The user should be prompted to enter the number.
def factorial(n):
    if n == 0:
        return 1

    else:
        return n * (n-1)

##Write a program that calculates the area and circumference of a circle. The user should be prompted to enter the radius of the circle.python
def find_area(radius):
    pie = 3.146
    area = pie * radius * radius
    return area

#Write a program that prompts the user to enter a sentence and then prints out the longest word in the sentence.
def find_longest(sentence):
    words = sentence.split(' ')
    longest_word = ''
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
        
        return longest_word

#Write a function that takes in an array of numbers and returns an array of unique values in ascending order, removing any duplicates.
def remove_duplicates(numbers):
   unique_arr = sorted(list(set(numbers)))
   return unique_arr

#Write a function that takes a string as a parameter and returns the string in reverse order.
def reverse_string(sentence):
    return sentence[::-1]

#Write a function that takes a list of strings as a parameter and returns a new list with all the strings in uppercase.
def new_list(words):
    newWord = words.split(" ")
    new_word = newWord.toUpperCase()
