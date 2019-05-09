import math


def paginas(s, l, c):
    mc = 0
    p = 0
    linhas = 1
    for i in s.split():
        if len(i) + mc <= c:
            mc += len(i) + 1
        else:
            mc = 0
            mc += len(i) + 1
            linhas += 1
    return math.ceil(linhas / l)


while True:
    try:
        n, l, c = input().split()
        n = int(n);
        l = int(l);
        c = int(c)
        s = input()
        print(paginas(s, l, c))

    except EOFError:
        break