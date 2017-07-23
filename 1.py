number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print("ура верно")
elif guess < number:
    print("число " + str(guess) + " меньше загаданного")
else:
    print("число " + str(guess) + " больше загаданного")



