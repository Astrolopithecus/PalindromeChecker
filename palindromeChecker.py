# Miles Philips
# prog 260
# 7-10-19
# Palindrome Detection program
from stack import Stack

#Implement this function that checks whether the input string is a palindrome:
# (a string where the characters of the string read the same when read backward
# as forward. E.g. racecar, mom)
def palindromeCheck(mystr):
    
    word = Stack()
    for char in mystr:
        word.push(char)

    while word.size() >=2:
        for char1 in mystr:
            char2 = word.pop()
            if char1 != char2:
                return False
    
    return True
       
def main():
    print("Welcome to the Palindrome check program.")    
    ans = 'y'
    while ans == 'y':
        expression = input("Enter the string you want to check: ")
        isAPalindrome = palindromeCheck(expression)
        if isAPalindrome:
            print(f"'{expression}' is a palindrome")
        else:
            print(f"'{expression}' is NOT a palindrome")
        ans = input("Continue?(y/n): ").lower()

    print("Goodbye")

if __name__ == "__main__":
    main()

        
