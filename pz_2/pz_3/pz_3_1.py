#Даны числа x, у. Проверить истинность высказывания: «Точка с координатами (x, у)
#лежит в первой или третьей координатной четверти»

def check_point(x, y):
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        return True
    else:
        return False

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

if check_point(x, y):
    print(f"Точка ({x}, {y}) находится в первой или третьей координатной четверти.")
else:
    print(f"Точка ({x}, {y}) не находится в первой или третьей координатной четверти.")