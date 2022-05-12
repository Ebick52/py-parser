def replaces(s: str, old: str, new: str):
    # like replace method of strings, but makes every replace seperately and returns all results
    for i in range(len(s) - len(old) + 1):
        if s[i:i+len(old)] == old:
            yield s[:i] + new + s[i+len(old):]

def parser(g: dict, w: str = ''):
    if w and not w.islower():
        raise ValueError
    queue, log, path = ['S'], 0, [-1]
    while queue:
        s = queue.pop(0)
        print('log {} : {}'.format(log, s))
        if s == w:
            p = [log]
            while(log):
                p.append(path[log])
                log = path[log]
            p.reverse()
            print('log path of answer:', *p)
            return True
        for i in g.keys():
            if i in s:
                for j in g[i]:
                    next = list(replaces(s, i, '')) if j == 'lambda' else list(replaces(s, i, j))
                    queue.extend(next)
                    path.extend([log for k in next])
        log += 1
    return False

def grammer():
    d, i = {}, 'S:'+input('S:')
    while i != 'end':
        i = i.split(':')
        assert isinstance(i, list)
        d[i[0]] = list(set(i[1].split('|')))
        i = input()
    return d

print(parser(grammer(), input('enter word: ')))
# Ebick
