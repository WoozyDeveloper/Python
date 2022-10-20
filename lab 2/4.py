def compose(notes, moves, start):
    ans = list()
    index = start
    ans.append(notes[index])
    for move in moves:
        index = (index + move) % len(notes)
        ans.append(notes[index])

    return ans


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, -2000], 2))
