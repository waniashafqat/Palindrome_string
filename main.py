# Program to check whether the user-entered string is a palindrome or not.
# This program is implemented using stack.

class Stack:
    # Special method to initialize the attributes.
    def __init__(self):
        self.s_data = []

    def push(self, val):
        self.s_data.append(val)

    def pop(self):
        return self.s_data.pop()

    def is_empty(self):
        return self.s_data == []

    def palindrome(self, lst):
        reversed_string = []

        for i in lst:
            self.push(i)

        while not self.is_empty():
            reversed_string.append(self.pop())

        # Check reversed string.
        if reversed_string == lst:
            return True

        else:
            return False


s = Stack()
lst = list(input("Please enter a string: "))

print("\nChecking whether the entered string is a 'palindrome' or not.")

if s.palindrome(lst):
    print("\nThe string is a palindrome.")

else:
    print("\nThe string is not a palindrome.")


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# This program is a bit optimized; to check whether a string is a palindrome or not.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

string = input("Please enter a string: ")
reversed_string = string[::-1]

stack = []

for letters in string:
    stack.append(letters)

print(stack)
print(reversed_string)

print("\nChecking whether the entered string is a 'palindrome' or not.")

if reversed_string == string:
    print("YES, The string is a palindrome.")

else:
    print("NO, The string is not a palindrome.")
