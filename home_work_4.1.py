# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(side_length_a, side_length_b, side_length_c):
    if ((side_length_a + side_length_b) <= side_length_c) or ((side_length_a + side_length_c) <= side_length_b) or (
            (side_length_b + side_length_c) <= side_length_a):
        type_triangle = 'Не треугольник'
    elif side_length_a == side_length_b == side_length_c:
        type_triangle = 'Равносторонний'
    elif (side_length_a == side_length_b) or (side_length_a == side_length_c) or (side_length_b == side_length_c):
        type_triangle = 'Равнобедренный'
    else:
        type_triangle = 'Обычный'
        # Здесь нужно написать код
    return type_triangle


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник"
]

for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
