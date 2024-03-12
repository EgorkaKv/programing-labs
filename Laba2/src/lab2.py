def suma(List):
    n = len(List) - 1
    for i in List:
        i[2] = i[0] + i[1] * n
    List.sort(key=lambda x: x[2])
    return sum([x[2] for x in List])


def buying(hamsters, S, C):
    for elem in hamsters:
        elem.append(elem[0]+elem[1]*(C-1))
        
    if suma(hamsters) <= S:
        return len(hamsters)
    else:
        left = 0
        right = len(hamsters) - 1
        while left <= right:
            center = (right + left) // 2

            if suma(hamsters[:center + 1]) == S:
                return center + 1
            if suma(hamsters[:center + 1]) > S:
                right = center - 1
            else:
                left = center + 1
        else:
            return center


if __name__ == '__main__':
    S = int(input())
    C = int(input())
    hamsters = list()

    for i in range(C):
        a, b = map(int, input().split())

    print(buying(hamsters,S,C))
