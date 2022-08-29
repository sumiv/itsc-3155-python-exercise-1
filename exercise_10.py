#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

user_string = input('Enter a string: ')

list = [*user_string]

for i in range(0, len(list), 3):
    x = i
    print(list[x:x+3])



