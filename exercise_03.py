#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

user_input = int(input('Enter an integer greater than 1: '))

for x in range(user_input + 1):
    cube_root = x*x*x
    print(f'The cube of {x} is {cube_root}')
