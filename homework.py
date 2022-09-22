# """ Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. """


# def inputNumber(inputText):
#     exam = False
#     while not exam:
#         try:
#             number = int(input(f"{inputText}"))
#             exam = True
#         except ValueError:
#             print("Введи число!")
#     return number


# def checkNumber(num):
#     if 6 <= num <= 7:
#         print("Да")
#     elif 0 < num < 6:
#         print("Нет")
#     else:
#         print("Введи число с 1 до 7!")


# num = inputNumber("Введите число: ")
# checkNumber(num)


# """ Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     newXYZ = []
#     for i in range(x):
#         newXYZ.append(input(f"Введите значение {xyz[i]}: "))
#     return newXYZ


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNumbers(3)

# if checkPredicate(statement) == True:
#     print(f"True")
# else:
#     print(f"False")


# """ Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). """


# def inputCoord(x):
#     a = [0] * x
#     for i in range(x):
#         exam = False
#         while not exam:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 exam = True
#                 if a[i] == 0:
#                     exam = False
#                     print("Координата не должно быть равна 0 ")
#             except ValueError:
#                 print("Введи число!")
#     return a


# def checkCoord(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"Точка находится в {text} четверти плоскости")


# koordinate = inputCoord(2)
# checkCoord(koordinate)


# """ Задача 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве. """


# def inputCoords(x):
#     xy = ["X", "Y"]
#     newXY = []
#     for i in range(x):
#         exam = False
#         while not exam:
#             try:
#                 number = int(input(f"Введите координату по {xy[i]}: "))
#                 newXY.append(number)
#                 exam = True
#             except ValueError:
#                 print("Введи целое число!")
#     return newXY


# def distanceCalculation(a, b):
#     distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return distance


# print("Введите координаты точки А")
# pointA = inputCoords(2)
# print("Введите координаты точки В")
# pointB = inputCoords(2)

# print(f"Длина отрезка: {format(distanceCalculation(pointA, pointB), '.2f')}")