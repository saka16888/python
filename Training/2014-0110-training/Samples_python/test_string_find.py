def f(w, strings):
    acc = []
    for s in strings:
        if s.find(w) > -1:
            acc.append(s)
    return acc
