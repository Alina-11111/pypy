#Task_5_7
from random import randint

number = randint(1,1000)
attempts = input('Введите количество попыток: ')
i = 0
while True:
    attempt = input('Введите целое число: ')
    i+=1
    if attempt == number:
        print('You are the winner')
        break
    if int(attempt) < number:
        print ('Ваше число меньше загаданного')
    else:
        print ('Ваше число больше загаданного ')
        
    if i == int(attempts):
        print(f'You are the loser, загаданное число: {number}')
        break
