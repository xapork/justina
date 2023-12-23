def l_finding(a, b):
    y = a['yb'] - a['ya']
    x = b['xb'] - b['xa']
    l = pow((pow(y, 2)) + pow(x, 2), 0.5)
    print(l)
    return l

l_finding({'yb': 5, 'ya': 2}, {'xb': 7, 'xa': 2})