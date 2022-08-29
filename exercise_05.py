#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

list_one = []
list_two = []
common_list = []

for x in range(5):
    user_input_one = input('Enter a number for the first list: ')
    list_one.insert(x, user_input_one)

for i in range(5):
    user_input_two = input('Enter a number for the second list: ')
    list_two.insert(i, user_input_two)

print('First List: ', list_one)
print('Second List: ',list_two)

# using intersection() : https://www.geeksforgeeks.org/python-intersection-two-lists/#:~:text=Intersection%20of%20two%20list%20means,the%20Intersection%20of%20the%20lists.
common_list = list(set(list_one).intersection(list_two))

print('Common List: ',common_list)