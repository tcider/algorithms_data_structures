def read_matrix_frominput():
    res = []
    size = int(input())
    for _ in range(size):
        line_list = input().split()
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        res.append(line_list)
    return size, res


def read_matrix_fromfile(file):
    res = []
    flag = 0
    with open(file, 'r') as tmp_file:
        for line in tmp_file.readlines():
            if not flag:
                size = int(line.split(',')[0])
                flag = 1
                continue
            line_list = line.split()
            if len(line_list) == 1:
                line_list = line.split(',')
            for i in range(len(line_list)):
                line_list[i] = int(line_list[i])
            res.append(line_list)
    return size, res


def read_edglist_frominput():
    res = []
    line_size = input().split(',')
    size1 = int(line_size[0])
    size2 = int(line_size[1])
    for _ in range(size2):
        line_list = input().split(',')
        for i in range(len(line_list)):
            line_list[i] = int(line_list[i])
        res.append(line_list)
    return size1, res


def read_adjlist_fromfile(file):
    res = []
    size = 0
    with open(file, 'r') as tmp_file:
        for line in tmp_file.readlines():
            line_list = line.split(':')
            line_list = line_list[1].split(',')
            for i in range(len(line_list)):
                line_list[i] = int(line_list[i])
            res.append(line_list)
            size += 1
    return size, res


def graf_printadj_bymatrix(graf):
    for line in graf:
        print(sum(line), ": ", end='')
        for i in range(len(line)):
            if line[i]:
                print(i + 1, " ", end='')
        print()


def graf_edg_tomatrix(size, graf):
    matrix = [[0] * size for _ in range(size)]
    for elem in graf:
        matrix[elem[0] - 1][elem[1] - 1] = 1
        matrix[elem[1] - 1][elem[0] - 1] = 1
    return matrix


def graf_adj_toedg(size, graf):
    res = set()
    for i in range(size):
        for elem in graf[i]:
            res.add((min(i + 1, elem), max(i + 1, elem)))
    return res


def read_edj_traversal(file):
    res = []
    flag = 0
    with open(file, 'r') as tmp_file:
        for line in tmp_file.readlines():
            line_list = line.split()
            if len(line_list) == 1:
                start = int(line_list[0])
                continue
            if not flag:
                size = int(line_list[0])
                flag = 1
            else:
                line_list[0] = int(line_list[0])
                line_list[1] = int(line_list[1])
                res.append(line_list)
    return size, res, start


def graf_matrix_toadj(graf):
    res = []
    for line in graf:
        tmp = []
        for i in range(len(line)):
            if line[i]:
                tmp.append(i + 1)
        res.append(tmp)
    return res


def dfs_traversal(v, graf, visited, traversal):
    traversal.append(v) # Записываем маршрут
    visited.add(v)  # Посетили вершину v
    for i in graf[v - 1]:  # Все смежные с v вершины
        if i not in visited:
            dfs_traversal(i, graf, visited, traversal) # Рекурсивно обходим смежные
            traversal.append(v) # После того как обошли смежные, фикисруем возврат в маршруте
    return


def main():
    print("Задание 1 - читаю матрицу смежности из matrix.txt")
    size, graf = read_matrix_fromfile("matrix.txt")
    for elem in graf:
        print(elem)
    print("Перевожу матрицу смежности в список смежности. Ответ - ")
    graf_printadj_bymatrix(graf)

    print("Задание 2 - читаю список ребер из edg_list.txt")
    size, graf = read_matrix_fromfile("edg_list.txt")
    for elem in graf:
        print(elem)
    graf = graf_edg_tomatrix(size, graf)
    print("Перевожу список ребер в список смежности. Ответ - ")
    graf_printadj_bymatrix(graf)

    print("Задание 4 - читаю список смежности из adj_list.txt")
    size, graf = read_adjlist_fromfile("adj_list.txt")
    for elem in graf:
        print(elem)
    print("Перевожу список смежности в список ребер. Ответ - ")
    graf = graf_adj_toedg(size, graf)
    for elem in graf:
        print(elem)

    print("Задание 5 - читаю список ребер из traversal.txt")
    size, graf, start = read_edj_traversal("traversal.txt")
    for elem in graf:
        print(elem)
    print("Перевожу список ребер в список смежности")
    graf = graf_edg_tomatrix(size, graf) # перевожу из списка ребер в матрицу смежности
    graf = graf_matrix_toadj(graf) # перевожу матрицу смежности в список смежности
    for elem in graf:
        print(elem)
    traversal = [] # Список для хранения пути
    visited = set()  # Множество удобно для хранения посещенных верщин
    start = 4
    dfs_traversal(start, graf, visited, traversal)  # start - начальная вершина обхода
    print("Ответ - ")
    print(len(traversal))
    for elem in traversal:
        print(elem, end=' ')


if __name__ == "__main__":
    main()
