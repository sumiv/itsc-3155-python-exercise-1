#Sumi Verma , Kaitlyn Finberg, Nathan Laney, Tyler Minnis, Honna Sammos

row_input = int(input('Enter a row num from 1 to 5: '))
col_input = int(input('Enter a col num from 1 to 5: '))

for i in range(1, 6):
    for x in range(1, 6):
        if i == row_input and x == col_input:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print('')
