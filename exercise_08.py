#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

og_list = []
once_list = []

for i in range(10):
    user_input = int(input(f'Enter number {i+1}: '))
    og_list.insert(i, user_input)

for x in og_list:
    if og_list.count(x) == 1:
        once_list.append(x)

print('Original List: ', og_list)
print('Nums that appear once: ',once_list)