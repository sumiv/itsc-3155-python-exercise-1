#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

number_input = input('Enter a number: ')
list = []
total = 0.0
avg = 0.0

for x in range(int(number_input)):
    float_num = float(input(f'Enter number {x+1}: '))
    list.insert(x, float_num)

    total += float_num
    avg = total/int(number_input)

print('List: ',list)
print('Average: ',avg)
