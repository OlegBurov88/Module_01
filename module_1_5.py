immutable_var = [1, 2], 1, 2, 1.0, 2.0, True, 'immutable_var'
print(immutable_var)
#immutable_var [1] = 2      # Элементы кортежа нельзя редактировать или как-либо изменять, кроме елементов списка внутри кортежа.
immutable_var [0][0] = 2
print(immutable_var)
mutable_list = [[1, 2], 1, 2, 1.0, 2.0, True, 'mutable_list']
print(mutable_list)
mutable_list [2] = mutable_list [0] * 2
print(mutable_list)