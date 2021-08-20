def full_name(first, last,):
    full_nam = first + ' ' + last
    return full_nam


while True:
    print('what is your name?')
    f_name = input('First name:')
    if f_name == 'quit':
        break
    l_name = input('Last name:')
    if l_name == 'quit':
        break

    new_name = full_name(f_name, l_name)
    print('\nhello, ' + new_name + '!')
# 函数的调用，
