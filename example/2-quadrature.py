def get_qud(num):
    # def temp_num(num_goal, k):
    #     temp = 1
    #     for i in range(1, num_goal + 1):
    #         temp *= i
    #     temp *= k
    #     return temp
    # output = temp_num(num_goal=num, k=1) if num > 0 else temp_num(num_goal=-num, k=-1)
    # return output
    temp_num = 1
    if num > 0:
        for i in range(1, num + 1):
            temp_num *= i
    else:
        for i in range(1, -num + 1):
            temp_num *= i
    return -temp_num


if __name__ == '__main__':

    number = -5
    result = get_qud(number)
    print(result)