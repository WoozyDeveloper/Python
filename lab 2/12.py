# Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.

# 	Example:

#          group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

def f(my_list):
    res = []
    seen = set()
    formed_list = []
    for word in my_list:
        if word not in seen:
            formed_list = [word]
            for word2 in my_list:
                if word2 not in seen and word != word2 and word[-2:] == word2[-2:]:
                    seen.add(word2)
                    formed_list.append(word2)
            formed_list.sort()
            if formed_list not in res:
                res.append(formed_list)
    return res


a = ['ana', 'banana', 'banana', 'carte', 'arme', 'parte']
print(f(a))
