def loop(dictionary):
    fr = []
    for i in range(1000):
        fr.append(0)

    res = []
    current_key = 'start'
    while True:
        value = dictionary.get(current_key)
        if fr[ord(value)] == 1:
            return res
        res.append(value)
        fr[ord(value)] = 1
        current_key = str(value)


print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z',
      'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
