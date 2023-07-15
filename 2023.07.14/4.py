hat_ches_prob_1 = input('Введите шахматный код первой клетки (например, а1):')
hat_ches_prob_2 = input('Введите шахматный код второй клетки (например, b2):')
hat_ches_prob_3 = ['a', 'c', 'e', 'g']
if hat_ches_prob_1[0] == hat_ches_prob_3[0] or hat_ches_prob_1[0] == hat_ches_prob_3[1] or hat_ches_prob_1[0] == hat_ches_prob_3[2] or hat_ches_prob_1[0] == hat_ches_prob_3[3]:
    a1 = 0
else: 
    a1 = 1
if hat_ches_prob_2[0] == hat_ches_prob_3[0] or hat_ches_prob_2[0] == hat_ches_prob_3[1] or hat_ches_prob_2[0] == hat_ches_prob_3[2] or hat_ches_prob_2[0] == hat_ches_prob_3[3]:
    a2 = 0
else: 
    a2 = 1
hat_ches_prob_4 = a1 + int(hat_ches_prob_1[1])
hat_ches_prob_5 = a2 + int(hat_ches_prob_2[1])
if (hat_ches_prob_4 + hat_ches_prob_5) % 2 == 0:
    print('Да')
else:
    print('Нет')
    
# ==== 4 ====
# Введите шахматный код первой клетки (например, а1):a1
# Введите шахматный код второй клетки (например, в2):b2
# Да
# Введите шахматный код первой клетки (например, а1):a1
# Введите шахматный код второй клетки (например, в2):e4
# Нет
# Введите шахматный код первой клетки (например, а1):f4
# Введите шахматный код второй клетки (например, в2):b7
# Нет


