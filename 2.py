number = 10
x = True
while x:

    key = int(input("введи число: " ))
    if key == number:
        print("угадала")
        break
    elif key < number:
        print("чуть больше")
    else:
        print("чуть менше")

else: print("Final")



# for i in range(1, 5, 2):
#     print(i)
#
#
#
# while True:
#     x = input("чтоугодно: ")
#     if x == "xxx":
#         break
#     print("Длинна строк: ", len(x))
# print("finish")


# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'exit':
#         print ("exit OK")
#         break
#     if len(s) < 3:
#         print('Слишком мало')
#         continue
#     print('Введённая строка достаточной длины')



