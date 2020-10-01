def parser(g: dict, w: str = ''):
    queue = ['S']
    while queue:
        s = queue.pop(0)
        print('log {} : {}'.format(log[0], s))
        log[0] += 1
        if s == w:
            return True
        for i in g.keys():
            if i in s:
                for j in g[i]:
                    queue.append(s.replace(i, j, 1))
    return False


def grammer():
    d, i = {}, 'S:'+input('S:')
    while i != 'end':
        i = i.split(':')
        assert isinstance(i, list)
        i[1] = i[1].split('|')
        d[i[0]] = i[1]
        i = input()
    return d


log = [0]
print(parser(grammer(), input('enter word: ')))
