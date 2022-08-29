# Sumi Verma, Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

first_input = input("Enter a string: ")
second_input = input("Enter another string: ")

# used python method endswith() : https://www.programiz.com/python-programming/methods/string/endswith
if first_input.endswith(second_input) or second_input.endswith(first_input):
    print('True')
else:
    print('False')
