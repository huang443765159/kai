# source_list = [2, 4, 6, 8]
# for idx, number in enumerate(source_list):
#     print('<{}> {}'.format(idx, number))

source = [[2, 4, 6, 8],
          [4, 6, 8, 10],
          [6, 8, 10, 12]]


# def finder(source_list, target):
#     result = None
#     for idx_y, one_line in enumerate(source_list):
#         for idx_x, number in enumerate(one_line):
#             if number == target:
#                 result = [idx_x, idx_y]
#     return result

def finder(source_list, target):
    result = None
    for idx_y, one_line in enumerate(source_list):
        if target in one_line:
            # 如果target不在里面，就可以停止
            for idx_x, number in enumerate(one_line):
                if target == number:
                    result = [idx_x, idx_y]
    return result


if __name__ == '__main__':

    num = 100
    bingo = finder(source, num)
    print('inout={} xy={}'.format(num, bingo))













