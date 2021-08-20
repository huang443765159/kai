a = [[1, 2], [2, 3], [3, 4], [5, 6], [2, 1]]


def search_pair(num_list):
    lens = len(num_list)
    num = 0
    for idx in range(lens):
        for idx1 in range(idx+1, lens):
            if num_list[idx][0] == num_list[idx1][0] and num_list[idx][1] == num_list[idx1][1]:
                num += 1
            elif num_list[idx][1] == num_list[idx1][0] and num_list[idx][0] == num_list[idx1][1]:
                num += 1
        return num


if __name__ == '__main__':

    pair = search_pair(a)
    print(pair)
