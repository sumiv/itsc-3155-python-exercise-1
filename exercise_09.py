#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

words = []
string = ''

for x in range(5):
    user_input = input('Enter a word: ')
    words.append(user_input)
    string += (f' {user_input}')

print('Words: ',words)
print('One String: ',string)
