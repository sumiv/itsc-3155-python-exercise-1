#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

user_input = ''
all_nums = []
even_nums = []

while user_input != 'QUIT':
    user_input = input('Enter a number or QUIT to quit: ')
    if user_input != 'QUIT':
        all_nums.append(user_input)
        if int(user_input) % 2 == 0:
            even_nums.append(user_input)

print('All Nums: ', all_nums)
print('Even Nums: ', even_nums)  