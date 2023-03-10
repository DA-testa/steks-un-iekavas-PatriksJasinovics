# Patriks Jasinovičs 221RDB082
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # Process opening bracket, write your code here
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            
        # Process closing bracket, write your code here
        if next in ")]}": 
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()
            

# Printing answer, write your code here
def main():
    text = input()
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        if not mismatch:
            print("Success")
        else:
            print(mismatch)


if __name__ == "__main__":
    main()
