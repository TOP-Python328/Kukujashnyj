a1 = input('Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):')
a2 = input('Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):')
if a1[0] == a2[0] and a1 != a2:
    print('Да')
elif a1[1] == a2[1] and a1 != a2:
    print('Да')
else:
    print('Нет')
    
# ==== 5 ====
# Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):d3
# Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):d8
# Да

# Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):d3
# Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):a1
# Нет

# Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):d3
# Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):d3
# Нет

# Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):h8
# Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):a8
# Да

# Введите шахматный код первой клетки (например, d4, но число - от 1 до 8):h8
# Введите шахматный код второй клетки (например, e4, но число - од 1 до 8):h1
# Да
