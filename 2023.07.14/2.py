# ПЕРЕИМЕНОВАТЬ: num1, num2
a1 = int(input('Введите первое целое число:'))
a2 = int(input('Введите второе целое число:'))
if a1 % a2 == 0:
    print(f'{a1} делится на {a2} нацело',
          f'частное: {int(a1 / a2)}',
          sep='\n')
else:
    print(f'{a1} не делится на {a2} нацело',
          f'неполное частное: {a1 // a2}',
          # ИСПРАВИТЬ: избыточное действие — вы уже вычисляли данное значение
          f'остаток: {a1 % a2}',
          sep='\n')


# Введите первое целое число:10
# Введите второе целое число:3
# 10 не делится на 3 нацело
# неполное частное: 3
# остаток: 1


# ИТОГ: хорошо — 2/3


# ИСПОЛЬЗОВАТЬ: а можно написать код так, чтобы не пришлось несколько раз генерировать практически одинаковые строки:
prompt = ' введите число > '
num1, num2 = int(input(prompt)), int(input(prompt))
rem = num1 % num2
ins1, ins2, ins3 = '', '', ''
if rem:
    ins1 = 'не '
    ins2 = 'неполное '
    ins3 = f'\nостаток: {rem}'
print(f'{num1} {ins1}делится на {num2} нацело\n{ins2}частное: {num1 // num2}{ins3}')
